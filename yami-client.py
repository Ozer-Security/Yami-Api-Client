import csv
import os
import json
import logging
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import click

from xlsxRenderer.renderer import (
    UserNameQueryResult,
    render_xlsx_hwid_report,
    render_xlsx_leak_report,
    render_xlsx_username_report,
)
from yamiClient.api.leaks import query_v1_leaks_query_get
from yamiClient.api.stealers import (
    search_hwid_v1_stealers_hwid_hwid_get,
    search_query_v1_stealers_search_get,
)
from yamiClient.client import AuthenticatedClient
from yamiClient.models.credential_item import CredentialItem
from yamiClient.models.credit_card_item import CreditCardItem
from yamiClient.models.http_validation_error import HTTPValidationError
from yamiClient.models.password_item import PasswordItem
from yamiClient.models.scalar_result import ScalarResult
from yamiClient.models.stealer_scalar_result import StealerScalarResult
from yamiClient.models.token_item import TokenItem
from yamiClient.models.user_log_item import UserLogItem

logger = logging.getLogger('Stealers_logger')
console_handler = logging.StreamHandler(sys.stdout)

formatter = logging.Formatter(
    fmt='%(asctime)s  %(process)-7s %(module)-20s %(message)s',
    datefmt='%Y-%m-%d- %H:%M:%S',
)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)


@dataclass
class CmdContext:
    domain: str
    priv_key_path: Path
    render_csv: bool = False
    render_xlsx: bool = False


BASE_URL = os.environ.get('YAMI_URL', 'http://localhost:8080')
OUTPUT_DIR = Path('.').parent.joinpath('query-results')
OUTPUT_DIR.mkdir(exist_ok=True)


@click.group()
@click.option(
    '-d',
    '--auth-domain',
    type=str,
    prompt=True,
    help='Domain to use for Yami authentication',
)
@click.option(
    '-k', '--priv-key-path', type=Path, prompt=True, help='Path to your private key'
)
@click.option('-c', '--csv', is_flag=True, help='Activate this flag for CSV output')
@click.option('-x', '--xlsx', is_flag=True, help='Activate this flag for xlsx output')
@click.pass_context
def cli(ctx, auth_domain: str, priv_key_path: Path, csv: bool, xlsx: bool):
    ctx.obj = CmdContext(auth_domain, priv_key_path, csv, xlsx)


@cli.group()
@click.pass_context
def eva001(ctx):
    pass


@eva001.command('search-domain')
@click.option(
    '-s',
    '--search-domain',
    type=str,
    required=True,
    help='Domain to search on leaks database',
)
@click.pass_context
def search_by_domain(ctx, search_domain: str):
    context: CmdContext = ctx.obj
    with AuthenticatedClient(
        base_url=BASE_URL, domain=context.domain, priv_key=context.priv_key_path
    ) as client:
        res = query_v1_leaks_query_get.sync(client=client, domain=search_domain)
        match res:
            case None:
                logger.info(f'No results found for domain {search_domain}')
            case HTTPValidationError() as e:
                logger.error(e.detail)
            case ScalarResult() as s:
                logger.info(
                    f'Found {s.total_result_count} leaks for domain {search_domain}'
                )
                ext = (
                    'xlsx'
                    if context.render_xlsx
                    else 'csv'
                    if context.render_csv
                    else 'json'
                )
                output_path = OUTPUT_DIR.joinpath(
                    f'leaks_result_{search_domain}_{int(time.time())}.{ext}'
                )
                data = [x.to_dict() for x in s.result]
                if data:
                    if context.render_xlsx:
                        data_classes_set = set()
                        for item in s.result:
                            data_classes_set |= set(item.dataclasses)
                        data_classes = sorted(list(data_classes_set))
                        render_xlsx_leak_report(output_path, s.result, data_classes)
                    elif context.render_csv:
                        header = list(data[0].keys())
                        with output_path.open(
                            'w', encoding='utf-8', newline=''
                        ) as output_file:
                            writer = csv.DictWriter(output_file, fieldnames=header)
                            writer.writeheader()
                            for d in data:
                                classes = ', '.join(d['dataclasses'])
                                d['dataclasses'] = classes
                                writer.writerow(d)
                    else:
                        with output_path.open(
                            'w', encoding='utf-8', newline=''
                        ) as output_file:
                            json.dump(data, output_file, ensure_ascii=False, indent=4)
                    logger.info(f'Query result saved in {output_path}')


@cli.group()
@click.pass_context
def eva002(ctx):
    pass


@eva002.command('hwid')
@click.option(
    '-w', '--hwid', type=str, required=True, help='Hwid to search on Stealers database'
)
@click.pass_context
def get_by_hwid(ctx, hwid: str):
    context: CmdContext = ctx.obj
    with AuthenticatedClient(
        base_url=BASE_URL, domain=context.domain, priv_key=context.priv_key_path
    ) as client:
        res = search_hwid_v1_stealers_hwid_hwid_get.sync(hwid=hwid, client=client)
        match res:
            case None:
                logger.info(f'No results found for HWID {hwid}')
            case HTTPValidationError() as e:
                logger.error(e.detail)
            case StealerScalarResult() as s:
                logger.info(f'Found {s.total_result_count} result for HWID {hwid}')
                ext = (
                    'xlsx'
                    if context.render_xlsx
                    else 'csv'
                    if context.render_csv
                    else 'json'
                )
                output_path = OUTPUT_DIR.joinpath(
                    f'stealers_result_{hwid}_{int(time.time())}.{ext}'
                )
                if s.result:
                    if context.render_xlsx:
                        render_xlsx_hwid_report(output_path, s.result)
                    elif context.render_csv:
                        with output_path.open(
                            'w', encoding='utf-8', newline=''
                        ) as output_file:
                            main_header = [
                                'hwid',
                                'telegram',
                                'build id',
                                'ip',
                                'date stolen',
                            ]
                            for r in s.result:
                                if r.credit_cards:
                                    header = main_header + [
                                        'holder',
                                        'card type',
                                        'card number',
                                        'expire date',
                                    ]
                                    writer = csv.writer(output_file)
                                    writer.writerow(header)
                                    for cc in r.credit_cards:
                                        writer.writerow(
                                            [
                                                r.user.hwid,
                                                r.user.telegram,
                                                r.user.build_id,
                                                r.user.ip,
                                                r.user.date,
                                            ]
                                            + [
                                                cc.holder,
                                                cc.card_type,
                                                cc.card,
                                                cc.expire_date,
                                            ]
                                        )
                                if r.tokens:
                                    header = main_header + ['token', 'token type']
                                    writer = csv.writer(output_file)
                                    writer.writerow(header)
                                    for t in r.tokens:
                                        writer.writerow(
                                            [
                                                r.user.hwid,
                                                r.user.telegram,
                                                r.user.build_id,
                                                r.user.ip,
                                                r.user.date,
                                            ]
                                            + [t.token, t.token_type]
                                        )
                                if r.rdp_credentials or r.ftp_credentials:
                                    header = main_header + [
                                        'server',
                                        'username',
                                        'password',
                                        'type',
                                    ]
                                    writer = csv.writer(output_file)
                                    writer.writerow(header)
                                    for cred in r.rdp_credentials:
                                        writer.writerow(
                                            [
                                                r.user.hwid,
                                                r.user.telegram,
                                                r.user.build_id,
                                                r.user.ip,
                                                r.user.date,
                                            ]
                                            + [
                                                cred.server,
                                                cred.user_name,
                                                cred.password,
                                                'RDP',
                                            ]
                                        )
                                    for cred in r.ftp_credentials:
                                        writer.writerow(
                                            [
                                                r.user.hwid,
                                                r.user.telegram,
                                                r.user.build_id,
                                                r.user.ip,
                                                r.user.date,
                                            ]
                                            + [
                                                cred.server,
                                                cred.user_name,
                                                cred.password,
                                                'FTP',
                                            ]
                                        )
                                if r.passwords:
                                    header = main_header + [
                                        'url',
                                        'username',
                                        'password',
                                    ]
                                    writer = csv.writer(output_file)
                                    writer.writerow(header)
                                    for p in r.passwords:
                                        writer.writerow(
                                            [
                                                r.user.hwid,
                                                r.user.telegram,
                                                r.user.build_id,
                                                r.user.ip,
                                                r.user.date,
                                            ]
                                            + [p.url, p.user_name, p.password]
                                        )
                    else:
                        with output_path.open(
                            'w', encoding='utf-8', newline=''
                        ) as output_file:
                            json.dump(
                                [x.to_dict() for x in s.result],
                                output_file,
                                ensure_ascii=False,
                                indent=4,
                            )
                    logger.info(f'Query result saved in {output_path}')


def _run_query(
    auth_domain: str, priv_key: Path, query: str
) -> (
    HTTPValidationError
    | list[CredentialItem | CreditCardItem | PasswordItem | TokenItem | UserLogItem]
    | None
):
    with AuthenticatedClient(
        base_url=BASE_URL, domain=auth_domain, priv_key=priv_key
    ) as client:
        return search_query_v1_stealers_search_get.sync(client=client, query=query)


@eva002.command('query')
@click.option('-q', '--yql-query', type=str, required=True, help='Run a YQL query')
@click.pass_context
def search_query(ctx, yql_query: str):
    context: CmdContext = ctx.obj
    res = _run_query(context.domain, context.priv_key_path, yql_query)
    match res:
        case None | []:
            logger.info(f'No results found for query {yql_query}')
        case HTTPValidationError() as e:
            logger.error(e.detail)
        case [*items]:
            logger.info(f'Found {len(items)} result for query {yql_query}')
            if context.render_xlsx:
                logger.warn(
                    'xlsx renderer not available for raw query results, defaulting to csv render'
                )
                context.render_csv = True
            ext = 'csv' if context.render_csv else 'json'
            output_path = OUTPUT_DIR.joinpath(
                f'stealers_query_result_{int(time.time())}.{ext}'
            )
            print(items[0])
            with output_path.open('w', encoding='utf-8', newline='') as output_file:
                if context.render_csv:
                    data = [x.to_dict() for x in items]
                    header = list(data[0].keys())
                    writer = csv.DictWriter(output_file, fieldnames=header)
                    writer.writeheader()
                    writer.writerows(data)
                else:
                    json.dump(
                        [x.to_dict() for x in items],
                        output_file,
                        ensure_ascii=False,
                        indent=4,
                    )
            logger.info(f'Query result saved in {output_path}')


@eva002.command('search-username')
@click.option(
    '-u',
    '--username',
    type=str,
    required=True,
    help='search all Leaks db for a given username',
)
@click.pass_context
def search_username(ctx, username: str):
    context: CmdContext = ctx.obj
    queries = [
        f'Passwords.Username: "{username}"',
        f'FTPCredentials.Username: "{username}"',
        f'RDPCredentials.Username: "{username}"',
    ]
    results: list[UserNameQueryResult] = []
    for query in queries:
        res = _run_query(context.domain, context.priv_key_path, query)
        match res:
            case None | []:
                logger.info(f'No results found for query {query}')
            case HTTPValidationError() as e:
                logger.error(e.detail)
            case [*items]:
                for item in items:
                    match item:
                        case CredentialItem() as c:
                            results.append(
                                UserNameQueryResult(
                                    hwid=c.hwid,
                                    telegram=c.telegram,
                                    build_id=c.build_id,
                                    ip=c.ip,
                                    leak_date=c.leak_date,
                                    url=c.server,
                                    user_name=c.user_name,
                                    password=c.password,
                                    credential_type=c.credential_type,
                                )
                            )
                        case PasswordItem() as p:
                            results.append(
                                UserNameQueryResult(
                                    hwid=p.hwid,
                                    telegram=p.telegram,
                                    build_id=p.build_id,
                                    ip=p.ip,
                                    leak_date=p.leak_date,
                                    url=p.url,
                                    user_name=p.username,
                                    password=p.password,
                                    credential_type='Password',
                                )
                            )
                        case _:
                            print(item)
    if results:
        logger.info(f'Found {len(results)} result for username {username}')
        ext = 'xlsx' if context.render_xlsx else 'csv' if context.render_csv else 'json'
        output_path = OUTPUT_DIR.joinpath(
            f'stealers_username_{username}_result_{int(time.time())}.{ext}'
        )
        if context.render_xlsx:
            render_xlsx_username_report(output_path, results)
        elif context.render_csv:
            with output_path.open('w', encoding='utf-8', newline='') as output_file:
                data = [x.to_dict() for x in results]
                header = list(data[0].keys())
                writer = csv.DictWriter(output_file, fieldnames=header)
                writer.writeheader()
                writer.writerows(data)
        else:
            with output_path.open('w', encoding='utf-8', newline='') as output_file:
                json.dump(
                    [x.to_dict() for x in results],
                    output_file,
                    ensure_ascii=False,
                    indent=4,
                )
        logger.info(f'Query result saved in {output_path}')


@eva002.command('search-domain')
@click.option(
    '-d',
    '--domain',
    type=str,
    required=True,
    help='search all Leaks db for a given domain',
)
@click.pass_context
def eva002_search_domain(ctx, domain: str):
    context: CmdContext = ctx.obj
    domain = domain.lower()
    if domain.startswith('http://'):
        domain = domain[7:]
    if domain.startswith('https://'):
        domain = domain[8:]
    queries = [
        f'Passwords.Url: ("{domain}", "https://{domain}", "http://{domain}")',
        f'FTPCredentials.Server: ("{domain}", "https://{domain}", "http://{domain}")',
        f'RDPCredentials.Server: ("{domain}", "https://{domain}", "http://{domain}")',
    ]
    results: list[UserNameQueryResult] = []
    for query in queries:
        res = _run_query(context.domain, context.priv_key_path, query)
        match res:
            case None | []:
                logger.info(f'No results found for query {query}')
            case HTTPValidationError() as e:
                logger.error(e.detail)
            case [*items]:
                for item in items:
                    match item:
                        case CredentialItem() as c:
                            results.append(
                                UserNameQueryResult(
                                    hwid=c.hwid,
                                    telegram=c.telegram,
                                    build_id=c.build_id,
                                    ip=c.ip,
                                    leak_date=c.leak_date,
                                    url=c.server,
                                    user_name=c.user_name,
                                    password=c.password,
                                    credential_type=c.credential_type,
                                )
                            )
                        case PasswordItem() as p:
                            results.append(
                                UserNameQueryResult(
                                    hwid=p.hwid,
                                    telegram=p.telegram,
                                    build_id=p.build_id,
                                    ip=p.ip,
                                    leak_date=p.leak_date,
                                    url=p.url,
                                    user_name=p.username,
                                    password=p.password,
                                    credential_type='Password',
                                )
                            )
                        case _:
                            print(item)
    if results:
        logger.info(f'Found {len(results)} result for domain {domain}')
        ext = 'xlsx' if context.render_xlsx else 'csv' if context.render_csv else 'json'
        output_path = OUTPUT_DIR.joinpath(
            f'stealers_domain_{domain}_result_{int(time.time())}.{ext}'
        )
        if context.render_xlsx:
            render_xlsx_username_report(output_path, results)
        elif context.render_csv:
            with output_path.open('w', encoding='utf-8', newline='') as output_file:
                data = [x.to_dict() for x in results]
                header = list(data[0].keys())
                writer = csv.DictWriter(output_file, fieldnames=header)
                writer.writeheader()
                writer.writerows(data)
        else:
            with output_path.open('w', encoding='utf-8', newline='') as output_file:
                json.dump(
                    [x.to_dict() for x in results],
                    output_file,
                    ensure_ascii=False,
                    indent=4,
                )
        logger.info(f'Query result saved in {output_path}')


if __name__ == '__main__':
    cli()
