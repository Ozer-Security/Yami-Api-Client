import builtins
from collections import defaultdict
from dataclasses import dataclass

from yamiClient.models.leak_query_result import LeakQueryResult
from xlsxRenderer.dataTable import DataTable, Header, ConditionnalFormatting


class BreachTypeAggregation:
    def __init__(self) -> None:
        self.breach_types: defaultdict[str, bool] = defaultdict(bool)

    def add_item(self, item: LeakQueryResult):
        for dc in item.dataclasses:
            self.breach_types[dc] = True

    def get_full_breaches_dict(self, all_data_classes: list[str]) -> dict[str, bool]:
        return {dc: self.breach_types[dc] for dc in all_data_classes}


class EmailAggregation(BreachTypeAggregation):
    def __init__(self) -> None:
        self.databases: set[tuple[str, str, str]] = set()
        super().__init__()

    def add_item(self, item: LeakQueryResult):
        self.databases.add((item.database, item.leak_date, ','.join(item.dataclasses)))
        super().add_item(item)

    @property
    def sorted_db(self) -> list[str]:
        return sorted(set([x[0] for x in self.databases]))

    @property
    def latest_password_breach(self) -> str:
        password_breaches = [
            x[1] for x in self.databases if 'password'.casefold() in x[2].casefold()
        ]
        if not password_breaches:
            return ''
        return max(password_breaches)


@dataclass
class BreachDatabase:
    name: str
    leak_date: str

    def __hash__(self) -> int:
        return hash((self.name, self.leak_date))

    @staticmethod
    def from_breach_model(item: LeakQueryResult) -> 'BreachDatabase':
        return BreachDatabase(item.database, item.leak_date)


class LeakQueryResultAggregator:
    def __init__(self, data: list[LeakQueryResult], data_classes: list[str]) -> None:
        self.data = data
        self.dataclasses = data_classes

    def _group_by_email(self) -> dict[str, EmailAggregation]:
        res: defaultdict[str, EmailAggregation] = defaultdict(EmailAggregation)
        for item in self.data:
            res[item.email].add_item(item)
        return dict(res)

    def _group_by_databases(self) -> dict[BreachDatabase, BreachTypeAggregation]:
        res: defaultdict[BreachDatabase, BreachTypeAggregation] = defaultdict(
            BreachTypeAggregation
        )
        for item in self.data:
            res[BreachDatabase.from_breach_model(item)].add_item(item)
        return dict(res)

    def group_by_email(self) -> DataTable:
        data = self._group_by_email()
        headers = (
            [Header(0, 'AccountEmail', builtins.str)]
            + [Header(1, 'Databases', builtins.str)]
            + [
                Header(
                    2,
                    'Last Password Breach Date',
                    builtins.str,
                    ConditionnalFormatting.REVERSE_GRADIENT,
                )
            ]
            + [
                Header(i + 3, name, builtins.bool, ConditionnalFormatting.BINARY)
                for i, name in enumerate(self.dataclasses)
            ]
        )
        dt = [
            {
                **{'AccountEmail': k},
                **{'Last Password Breach Date': v.latest_password_breach},
                **{'Databases': ', '.join(v.sorted_db)},
                **{dc: v.breach_types[dc] for dc in self.dataclasses},
            }
            for k, v in data.items()
        ]
        return DataTable(headers, dt)

    def group_by_databases(self) -> DataTable:
        data = self._group_by_databases()
        headers = [
            Header(0, 'Name', builtins.str),
            Header(
                1, 'Breach Date', builtins.str, ConditionnalFormatting.REVERSE_GRADIENT
            ),
        ] + [
            Header(i + 2, name, builtins.bool, ConditionnalFormatting.BINARY)
            for i, name in enumerate(self.dataclasses)
        ]
        dt = [
            {
                **{'Name': k.name, 'Breach Date': k.leak_date},
                **{dc: v.breach_types[dc] for dc in self.dataclasses},
            }
            for k, v in data.items()
        ]
        return DataTable(headers, dt)
