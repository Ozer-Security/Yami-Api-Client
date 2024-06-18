from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.new_user import NewUser
from ...models.user_base import UserBase
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: NewUser,
    x_yami_domain: Union[None, Unset, str] = UNSET,
    x_yami_token: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(x_yami_domain, Unset):
        headers['x-yami-domain'] = x_yami_domain

    if not isinstance(x_yami_token, Unset):
        headers['x-yami-token'] = x_yami_token

    _kwargs: Dict[str, Any] = {
        'method': 'post',
        'url': '/v1/admin/create-user',
    }

    _body = body.to_dict()

    _kwargs['json'] = _body
    headers['Content-Type'] = 'application/json'

    _kwargs['headers'] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, UserBase]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserBase.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, UserBase]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewUser,
    x_yami_domain: Union[None, Unset, str] = UNSET,
    x_yami_token: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, UserBase]]:
    """Get Admin

    Args:
        x_yami_domain (Union[None, Unset, str]):
        x_yami_token (Union[None, Unset, str]):
        body (NewUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, UserBase]]
    """

    kwargs = _get_kwargs(
        body=body,
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
    body: NewUser,
    x_yami_domain: Union[None, Unset, str] = UNSET,
    x_yami_token: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, UserBase]]:
    """Get Admin

    Args:
        x_yami_domain (Union[None, Unset, str]):
        x_yami_token (Union[None, Unset, str]):
        body (NewUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, UserBase]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_yami_domain=x_yami_domain,
        x_yami_token=x_yami_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewUser,
    x_yami_domain: Union[None, Unset, str] = UNSET,
    x_yami_token: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, UserBase]]:
    """Get Admin

    Args:
        x_yami_domain (Union[None, Unset, str]):
        x_yami_token (Union[None, Unset, str]):
        body (NewUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, UserBase]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_yami_domain=x_yami_domain,
        x_yami_token=x_yami_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewUser,
    x_yami_domain: Union[None, Unset, str] = UNSET,
    x_yami_token: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, UserBase]]:
    """Get Admin

    Args:
        x_yami_domain (Union[None, Unset, str]):
        x_yami_token (Union[None, Unset, str]):
        body (NewUser):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, UserBase]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_yami_domain=x_yami_domain,
            x_yami_token=x_yami_token,
        )
    ).parsed
