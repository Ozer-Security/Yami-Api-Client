from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.scalar_result import ScalarResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    domain: Union[Unset, str] = '',
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 0,
    x_yami_domain: Union[None, Unset, str] = UNSET,
    x_yami_token: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(x_yami_domain, Unset):
        headers['x-yami-domain'] = x_yami_domain

    if not isinstance(x_yami_token, Unset):
        headers['x-yami-token'] = x_yami_token

    params: Dict[str, Any] = {}

    params['domain'] = domain

    params['skip'] = skip

    params['limit'] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/v1/leaks/query',
        'params': params,
    }

    _kwargs['headers'] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, ScalarResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ScalarResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, ScalarResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    domain: Union[Unset, str] = '',
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 0,
    x_yami_domain: Union[None, Unset, str] = UNSET,
    x_yami_token: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ScalarResult]]:
    """Query

    Args:
        domain (Union[Unset, str]):  Default: ''.
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 0.
        x_yami_domain (Union[None, Unset, str]):
        x_yami_token (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ScalarResult]]
    """

    kwargs = _get_kwargs(
        domain=domain,
        skip=skip,
        limit=limit,
        x_yami_domain=x_yami_domain,
        x_yami_token=x_yami_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    domain: Union[Unset, str] = '',
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 0,
    x_yami_domain: Union[None, Unset, str] = UNSET,
    x_yami_token: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ScalarResult]]:
    """Query

    Args:
        domain (Union[Unset, str]):  Default: ''.
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 0.
        x_yami_domain (Union[None, Unset, str]):
        x_yami_token (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ScalarResult]
    """

    return sync_detailed(
        client=client,
        domain=domain,
        skip=skip,
        limit=limit,
        x_yami_domain=x_yami_domain,
        x_yami_token=x_yami_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    domain: Union[Unset, str] = '',
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 0,
    x_yami_domain: Union[None, Unset, str] = UNSET,
    x_yami_token: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ScalarResult]]:
    """Query

    Args:
        domain (Union[Unset, str]):  Default: ''.
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 0.
        x_yami_domain (Union[None, Unset, str]):
        x_yami_token (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ScalarResult]]
    """

    kwargs = _get_kwargs(
        domain=domain,
        skip=skip,
        limit=limit,
        x_yami_domain=x_yami_domain,
        x_yami_token=x_yami_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    domain: Union[Unset, str] = '',
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 0,
    x_yami_domain: Union[None, Unset, str] = UNSET,
    x_yami_token: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ScalarResult]]:
    """Query

    Args:
        domain (Union[Unset, str]):  Default: ''.
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 0.
        x_yami_domain (Union[None, Unset, str]):
        x_yami_token (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ScalarResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            domain=domain,
            skip=skip,
            limit=limit,
            x_yami_domain=x_yami_domain,
            x_yami_token=x_yami_token,
        )
    ).parsed
