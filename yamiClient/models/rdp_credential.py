from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar('T', bound='RDPCredential')


@_attrs_define
class RDPCredential:
    """
    Attributes:
        server (Union[None, str]):
        user_name (Union[None, str]):
        password (Union[None, str]):
        user_log_id (str):
        id (Union[Unset, str]):
    """

    server: Union[None, str]
    user_name: Union[None, str]
    password: Union[None, str]
    user_log_id: str
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server: Union[None, str]
        server = self.server

        user_name: Union[None, str]
        user_name = self.user_name

        password: Union[None, str]
        password = self.password

        user_log_id = self.user_log_id

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'server': server,
                'user_name': user_name,
                'password': password,
                'user_log_id': user_log_id,
            }
        )
        if id is not UNSET:
            field_dict['id'] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_server(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        server = _parse_server(d.pop('server'))

        def _parse_user_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        user_name = _parse_user_name(d.pop('user_name'))

        def _parse_password(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        password = _parse_password(d.pop('password'))

        user_log_id = d.pop('user_log_id')

        id = d.pop('id', UNSET)

        rdp_credential = cls(
            server=server,
            user_name=user_name,
            password=password,
            user_log_id=user_log_id,
            id=id,
        )

        rdp_credential.additional_properties = d
        return rdp_credential

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
