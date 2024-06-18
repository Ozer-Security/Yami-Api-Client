from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar('T', bound='Token')


@_attrs_define
class Token:
    """
    Attributes:
        token (Union[None, str]):
        token_type (Union[None, str]):
        user_log_id (str):
        id (Union[Unset, str]):
    """

    token: Union[None, str]
    token_type: Union[None, str]
    user_log_id: str
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token: Union[None, str]
        token = self.token

        token_type: Union[None, str]
        token_type = self.token_type

        user_log_id = self.user_log_id

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'token': token,
                'token_type': token_type,
                'user_log_id': user_log_id,
            }
        )
        if id is not UNSET:
            field_dict['id'] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_token(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        token = _parse_token(d.pop('token'))

        def _parse_token_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        token_type = _parse_token_type(d.pop('token_type'))

        user_log_id = d.pop('user_log_id')

        id = d.pop('id', UNSET)

        token = cls(
            token=token,
            token_type=token_type,
            user_log_id=user_log_id,
            id=id,
        )

        token.additional_properties = d
        return token

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
