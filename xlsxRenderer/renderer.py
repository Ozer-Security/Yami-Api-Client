import builtins
from collections import defaultdict
from dataclasses import dataclass
import xlsxwriter
from pathlib import Path
from datetime import datetime
from itertools import cycle

from xlsxRenderer.dataTable import DataTable, ConditionnalFormatting, Header, T
from xlsxRenderer.dataAggregators import LeakQueryResultAggregator
from yamiClient.models.leak_query_result import LeakQueryResult
from yamiClient.models.stealers_query_result import StealersQueryResult


def colname(col: int) -> str:
    digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    ival = col + 1
    while True:
        res += digits[(ival - 1) % 26]
        ival = (ival - 1) // 26
        if not ival:
            break
    return res[::-1]


class XlsxRenderer:
    def __init__(self, output_file: Path) -> None:
        self.output_dir = output_file.parent
        self.file_name = output_file.name
        self.output_file_path = output_file
        self.output_dir.mkdir(exist_ok=True)
        self.worksheets: dict[str, xlsxwriter.workbook.Worksheet] = {}

        self.wb = xlsxwriter.Workbook(self.output_file_path)
        self.color_cycle = cycle([ 
            self.wb.add_format({'bg_color': '#167288'}),
            self.wb.add_format({'bg_color': '#8CDAEC'}),
            self.wb.add_format({'bg_color': '#B45248'}),
            self.wb.add_format({'bg_color': '#D48C84'}),
            self.wb.add_format({'bg_color': '#A89A49'}),
            self.wb.add_format({'bg_color': '#D6CFA2'}),
            self.wb.add_format({'bg_color': '#3CB464'}),
            self.wb.add_format({'bg_color': '#9BDDB1'}),
            self.wb.add_format({'bg_color': '#643C6A'}),
            self.wb.add_format({'bg_color': '#836394'})
        ])
        self.color_val_dict = defaultdict(self.color_cycle.__next__)
        self.formats = {
            'percentage_format': self.wb.add_format({'num_format': '0.00%'}),
            'date_format': self.wb.add_format({'num_format': 'yyyy-mm-dd'}),
            'bold': self.wb.add_format({'bold': True}),
            'light_red': self.wb.add_format(
                {'bg_color': '#FFC7CE', 'fg_color': '#9C0006'}
            ),
            'light_green': self.wb.add_format(
                {'bg_color': '#C6EFCE', 'fg_color': '#C6EFCE'}
            ),
            'basic_gradient': {
                'type': '3_color_scale',
                'min_type': 'min',
                'mid_type': 'percentile',
                'max_type': 'max',
            },
            'green_yellow_red': {
                'min_color': '#63BE7B',
                'mid_color': '#FFEB84',
                'max_color': '#F8696B',
            },
            'red_yellow_green': {
                'min_color': '#F8696B',
                'mid_color': '#FFEB84',
                'max_color': '#63BE7B',
            },
        }

    def __enter__(self) -> 'XlsxRenderer':
        return self

    def _next_color(self, val: T) -> str:
        return self.color_val_dict[val]

    def add_sheet(self, name: str):
        self.worksheets[name] = self.wb.add_worksheet(name=name)

    def render_datatable(
        self, data_table: DataTable, sheet_name: str, aggregate: bool = False
    ):
        worksheet = self.worksheets[sheet_name]
        row, col = 0, 0

        hvalues = sorted(data_table.headers, key=lambda x: x.position)
        for hval in hvalues:
            worksheet.write_string(
                row, col, hval.name, cell_format=self.formats['bold']
            )
            col += 1
        row += 1
        col = 0
        for dt_val in data_table.data:
            for hval in hvalues:
                cell_format = None
                if col == 0:
                    cell_format = self.formats['bold']
                val = dt_val.get(hval.name, None)
                if hval.conditional_formatting == ConditionnalFormatting.COLOR_CYCLE and col != 0:
                    cell_format = self._next_color(val)
                type_name = hval.htype
                if val is None:
                    val = 'N/A'
                    type_name = builtins.str
                match type_name:
                    case builtins.str:
                        if val != '' and val != 'N/A' and hval.name in {
                            'Breach Date',
                            'Last Password Breach Date',
                            'date'
                        }:
                            worksheet.write_datetime(
                                row,
                                col,
                                datetime.strptime(val, '%Y-%m-%d'),
                                cell_format=self.formats['date_format'],
                            )
                        else:
                            worksheet.write_string(
                                row, col, val, cell_format=cell_format
                            )
                    case builtins.bool:
                        worksheet.write_boolean(row, col, val, cell_format=cell_format)
                    case builtins.int:
                        worksheet.write_number(row, col, val, cell_format=cell_format)
                    case builtins.float:
                        worksheet.write_number(row, col, val, cell_format=cell_format)
                    case builtins.bytes:
                        worksheet.write_string(
                            row, col, val.decode('utf-8'), cell_format=cell_format
                        )
                    case _:
                        worksheet.write_string(
                            row, col, str(val), cell_format=cell_format
                        )
                col += 1
            col = 0
            row += 1
        if aggregate:
            start_col = None
            for hval in hvalues:
                if hval.htype == builtins.bool:
                    current_colname = colname(col)
                    if start_col is None:
                        start_col = current_colname
                    range = f'{current_colname}{row-len(data_table.data)+1}:{current_colname}{row}'
                    worksheet.write_formula(row, col, f'=COUNTIF({range},TRUE)')
                    worksheet.write_formula(
                        row + 1,
                        col,
                        f'={current_colname}{row+1}/COUNTA({range})',
                        cell_format=self.formats['percentage_format'],
                    )
                col += 1
            range = f'{start_col}{row+1}:{colname(col-1)}{row+2}'
            worksheet.conditional_format(
                range,
                {**self.formats['basic_gradient'], **self.formats['green_yellow_red']},
            )

        col = 0
        for hval in hvalues:
            current_colname = colname(col)
            range = (
                f'{current_colname}{row-len(data_table.data)+1}:{current_colname}{row}'
            )
            if hval.conditional_formatting == ConditionnalFormatting.BINARY:
                worksheet.conditional_format(
                    range,
                    {
                        'type': 'cell',
                        'criteria': '=',
                        'value': 'TRUE',
                        'format': self.formats['light_red'],
                    },
                )
                worksheet.conditional_format(
                    range,
                    {
                        'type': 'cell',
                        'criteria': '=',
                        'value': 'FALSE',
                        'format': self.formats['light_green'],
                    },
                )
            if hval.conditional_formatting == ConditionnalFormatting.GRADIENT:
                worksheet.conditional_format(
                    range,
                    {
                        **self.formats['basic_gradient'],
                        **self.formats['red_yellow_green'],
                    },
                )
            if hval.conditional_formatting == ConditionnalFormatting.REVERSE_GRADIENT:
                worksheet.conditional_format(
                    range,
                    {
                        **self.formats['basic_gradient'],
                        **self.formats['green_yellow_red'],
                    },
                )
            col += 1

    def __exit__(self, exc_type, exc_value, tb):
        for ws in self.worksheets.values():
            ws.autofit()
        self.wb.close()


@dataclass
class UserNameQueryResult:
    hwid: str | None
    telegram: str | None
    build_id: str | None
    ip: str | None
    leak_date: str | None
    url: str | None
    user_name: str | None
    password: str | None
    credential_type: str | None

    def to_dict(self) -> dict[str, str | None]:
        return self.__dict__


@dataclass
class CredentialResult:
    hwid: str | None
    url: str | None
    user_name: str | None
    password: str | None
    credential_type: str | None

    def to_dict(self) -> dict[str, str | None]:
        return self.__dict__


@dataclass
class TokenResult:
    hwid: str | None
    token: str | None
    token_type: str | None

    def to_dict(self) -> dict[str, str | None]:
        return self.__dict__


@dataclass
class CreditCardResult:
    hwid: str | None
    holder: str | None
    card_type: str | None
    card_number: str | None
    expire_date: str | None

    def to_dict(self) -> dict[str, str | None]:
        return self.__dict__


@dataclass
class FileResult:
    hwid: str | None
    file_name: str | None

    def to_dict(self) -> dict[str, str | None]:
        return self.__dict__


def render_xlsx_leak_report(
    output_file_path: Path, breaches: list[LeakQueryResult], data_classes: list[str]
):
    aggregation = LeakQueryResultAggregator(breaches, data_classes)
    with XlsxRenderer(output_file_path) as renderer:
        renderer.add_sheet('Emails')
        renderer.render_datatable(
            aggregation.group_by_email(), 'Emails', aggregate=True
        )

        renderer.add_sheet('Database')
        renderer.render_datatable(
            aggregation.group_by_databases(), 'Database', aggregate=False
        )

        rawdata = [x.to_dict() for x in breaches]
        str_rawdata = []
        for item in rawdata:
            item['dataclasses'] = ', '.join(item['dataclasses'])
            str_rawdata.append(item)
        renderer.add_sheet('rawdata')
        renderer.render_datatable(
            DataTable(
                [
                    Header(
                        i,
                        name,
                        builtins.bool
                        if name.startswith('Is') or name.startswith('Contains')
                        else builtins.str,
                    )
                    for i, name in enumerate(rawdata[0].keys())
                ],
                str_rawdata,
            ),
            'rawdata',
        )


def render_xlsx_hwid_report(output_file_path: Path, records: list[StealersQueryResult]):
    with XlsxRenderer(output_file_path) as renderer:
        renderer.add_sheet('Infos')
        info_data_table = DataTable(
            [
                Header(i, col, builtins.str)
                for i, col in enumerate(['hwid', 'ip', 'date'])
            ] + [
                Header(3, 'build_id', builtins.str, ConditionnalFormatting.COLOR_CYCLE),
                Header(4, 'telegram', builtins.str)
            ],
            [x.user.to_dict() for x in records],
        )
        renderer.render_datatable(info_data_table, 'Infos')
        creds: list[CredentialResult] = []
        tokens: list[TokenResult] = []
        cards: list[CreditCardResult] = []
        files: list[FileResult] = []
        for item in records:
            creds.extend(
                [
                    CredentialResult(
                        item.user.hwid, p.url, p.user_name, p.password, 'Password'
                    )
                    for p in item.passwords
                ]
            )
            creds.extend(
                [
                    CredentialResult(
                        item.user.hwid, f.server, f.user_name, f.password, 'FTP'
                    )
                    for f in item.ftp_credentials
                ]
            )
            creds.extend(
                [
                    CredentialResult(
                        item.user.hwid, r.server, r.user_name, r.password, 'RDP'
                    )
                    for r in item.rdp_credentials
                ]
            )
            tokens.extend(
                [
                    TokenResult(item.user.hwid, t.token, t.token_type)
                    for t in item.tokens
                ]
            )
            cards.extend(
                [
                    CreditCardResult(
                        item.user.hwid, cc.holder, cc.card_type, cc.card, cc.expire_date
                    )
                    for cc in item.credit_cards
                ]
            )
            files.extend(
                [FileResult(item.user.hwid, f.file_name) for f in item.stolen_files]
            )
        if creds:
            renderer.add_sheet('Credentials')
            cred_data_table = DataTable(
                [
                    Header(i, col, builtins.str)
                    for i, col in enumerate(
                        ['hwid', 'url', 'user_name', 'password', 'credential_type']
                    )
                ],
                [x.to_dict() for x in creds],
            )
            renderer.render_datatable(cred_data_table, 'Credentials')
        if tokens:
            renderer.add_sheet('Tokens')
            token_data_table = DataTable(
                [
                    Header(i, col, builtins.str)
                    for i, col in enumerate(['hwid', 'token', 'token_type'])
                ],
                [x.to_dict() for x in tokens],
            )
            renderer.render_datatable(token_data_table, 'Tokens')
        if cards:
            renderer.add_sheet('Cards')
            card_data_table = DataTable(
                [
                    Header(i, col, builtins.str)
                    for i, col in enumerate(
                        ['hwid', 'holder', 'card_type', 'card_number', 'expire_date']
                    )
                ],
                [x.to_dict() for x in cards],
            )
            renderer.render_datatable(card_data_table, 'Cards')
        if files:
            renderer.add_sheet('Stolen Files')
            file_data_table = DataTable(
                [
                    Header(i, col, builtins.str)
                    for i, col in enumerate(['hwid', 'file_name'])
                ],
                [x.to_dict() for x in files],
            )
            renderer.render_datatable(file_data_table, 'Stolen Files')


def render_xlsx_username_report(
    output_file_path: Path, records: list[UserNameQueryResult]
):
    with XlsxRenderer(output_file_path) as renderer:
        renderer.add_sheet('Username match')
        data_table = DataTable(
            [
                Header(i, col, builtins.str)
                for i, col in enumerate(
                    [
                        'hwid',
                        'ip',
                        'date',
                    ]
                )
            ] + [
                Header(3, 'build_id', builtins.str, ConditionnalFormatting.COLOR_CYCLE),
            ] + [
                Header(i+4, col, builtins.str)
                for i, col in enumerate(
                    [
                        'telegram',
                        'url',
                        'user_name',
                        'password',
                        'credential_type',
                    ]
                )
            ],
            [x.to_dict() for x in records],
        )
        renderer.render_datatable(data_table, 'Username match')
