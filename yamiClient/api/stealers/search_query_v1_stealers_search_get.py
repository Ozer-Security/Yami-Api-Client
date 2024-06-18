from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.credential_item import CredentialItem
from ...models.credit_card_item import CreditCardItem
from ...models.http_validation_error import HTTPValidationError
from ...models.password_item import PasswordItem
from ...models.token_item import TokenItem
from ...models.user_log_item import UserLogItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
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

    params['query'] = query

    params['skip'] = skip

    params['limit'] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        'method': 'get',
        'url': '/v1/stealers/search',
        'params': params,
    }

    _kwargs['headers'] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        HTTPValidationError,
        List[
            Union[
                'CredentialItem',
                'CreditCardItem',
                'PasswordItem',
                'TokenItem',
                'UserLogItem',
            ]
        ],
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(
                data: object,
            ) -> Union[
                'CredentialItem',
                'CreditCardItem',
                'PasswordItem',
                'TokenItem',
                'UserLogItem',
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    if 'url' in data.keys():
                        response_200_item_type_1 = PasswordItem.from_dict(data)

                        return response_200_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    if 'holder' in data.keys():
                        response_200_item_type_2 = CreditCardItem.from_dict(data)

                        return response_200_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    if 'token' in data.keys():
                        response_200_item_type_3 = TokenItem.from_dict(data)

                        return response_200_item_type_3
                except:  # noqa: E722
                    pass

                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    if 'server' in data.keys():
                        response_200_item_type_4 = CredentialItem.from_dict(data)

                        return response_200_item_type_4
                except:  # noqa: E722
                    pass

                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_type_0 = UserLogItem.from_dict(data)

                return response_200_item_type_0

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[
    Union[
        HTTPValidationError,
        List[
            Union[
                'CredentialItem',
                'CreditCardItem',
                'PasswordItem',
                'TokenItem',
                'UserLogItem',
            ]
        ],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 0,
    x_yami_domain: Union[None, Unset, str] = UNSET,
    x_yami_token: Union[None, Unset, str] = UNSET,
) -> Response[
    Union[
        HTTPValidationError,
        List[
            Union[
                'CredentialItem',
                'CreditCardItem',
                'PasswordItem',
                'TokenItem',
                'UserLogItem',
            ]
        ],
    ]
]:
    """Search Query

    Args:
        query (str):
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 0.
        x_yami_domain (Union[None, Unset, str]):
        x_yami_token (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List[Union['CredentialItem', 'CreditCardItem', 'PasswordItem', 'TokenItem', 'UserLogItem']]]]
    """

    kwargs = _get_kwargs(
        query=query,
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
    query: str,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 0,
    x_yami_domain: Union[None, Unset, str] = UNSET,
    x_yami_token: Union[None, Unset, str] = UNSET,
) -> Optional[
    Union[
        HTTPValidationError,
        List[
            Union[
                'CredentialItem',
                'CreditCardItem',
                'PasswordItem',
                'TokenItem',
                'UserLogItem',
            ]
        ],
    ]
]:
    """Search Query

    Args:
        query (str):
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 0.
        x_yami_domain (Union[None, Unset, str]):
        x_yami_token (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List[Union['CredentialItem', 'CreditCardItem', 'PasswordItem', 'TokenItem', 'UserLogItem']]]
    """

    return sync_detailed(
        client=client,
        query=query,
        skip=skip,
        limit=limit,
        x_yami_domain=x_yami_domain,
        x_yami_token=x_yami_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 0,
    x_yami_domain: Union[None, Unset, str] = UNSET,
    x_yami_token: Union[None, Unset, str] = UNSET,
) -> Response[
    Union[
        HTTPValidationError,
        List[
            Union[
                'CredentialItem',
                'CreditCardItem',
                'PasswordItem',
                'TokenItem',
                'UserLogItem',
            ]
        ],
    ]
]:
    """Search Query

    Args:
        query (str):
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 0.
        x_yami_domain (Union[None, Unset, str]):
        x_yami_token (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List[Union['CredentialItem', 'CreditCardItem', 'PasswordItem', 'TokenItem', 'UserLogItem']]]]
    """

    kwargs = _get_kwargs(
        query=query,
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
    query: str,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 0,
    x_yami_domain: Union[None, Unset, str] = UNSET,
    x_yami_token: Union[None, Unset, str] = UNSET,
) -> Optional[
    Union[
        HTTPValidationError,
        List[
            Union[
                'CredentialItem',
                'CreditCardItem',
                'PasswordItem',
                'TokenItem',
                'UserLogItem',
            ]
        ],
    ]
]:
    """Search Query

    Args:
        query (str):
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 0.
        x_yami_domain (Union[None, Unset, str]):
        x_yami_token (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List[Union['CredentialItem', 'CreditCardItem', 'PasswordItem', 'TokenItem', 'UserLogItem']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            skip=skip,
            limit=limit,
            x_yami_domain=x_yami_domain,
            x_yami_token=x_yami_token,
        )
    ).parsed
