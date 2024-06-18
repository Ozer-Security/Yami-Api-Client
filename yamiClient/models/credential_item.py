from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar('T', bound='CredentialItem')


@_attrs_define
class CredentialItem:
    """
    Attributes:
        hwid (str):
        telegram (Union[None, str]):
        build_id (Union[None, str]):
        ip (Union[None, str]):
        leak_date (Union[None, str]):
        server (Union[None, str]):
        user_name (Union[None, str]):
        password (Union[None, str]):
        credential_type (str):
    """

    hwid: str
    telegram: Union[None, str]
    build_id: Union[None, str]
    ip: Union[None, str]
    leak_date: Union[None, str]
    server: Union[None, str]
    user_name: Union[None, str]
    password: Union[None, str]
    credential_type: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hwid = self.hwid

        telegram: Union[None, str]
        telegram = self.telegram

        build_id: Union[None, str]
        build_id = self.build_id

        ip: Union[None, str]
        ip = self.ip

        leak_date: Union[None, str]
        leak_date = self.leak_date

        server: Union[None, str]
        server = self.server

        user_name: Union[None, str]
        user_name = self.user_name

        password: Union[None, str]
        password = self.password

        credential_type = self.credential_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'hwid': hwid,
                'telegram': telegram,
                'buildId': build_id,
                'ip': ip,
                'leakDate': leak_date,
                'server': server,
                'userName': user_name,
                'password': password,
                'credentialType': credential_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hwid = d.pop('hwid')

        def _parse_telegram(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        telegram = _parse_telegram(d.pop('telegram'))

        def _parse_build_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        build_id = _parse_build_id(d.pop('buildId'))

        def _parse_ip(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        ip = _parse_ip(d.pop('ip'))

        def _parse_leak_date(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        leak_date = _parse_leak_date(d.pop('leakDate'))

        def _parse_server(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        server = _parse_server(d.pop('server'))

        def _parse_user_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        user_name = _parse_user_name(d.pop('userName'))

        def _parse_password(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        password = _parse_password(d.pop('password'))

        credential_type = d.pop('credentialType')

        credential_item = cls(
            hwid=hwid,
            telegram=telegram,
            build_id=build_id,
            ip=ip,
            leak_date=leak_date,
            server=server,
            user_name=user_name,
            password=password,
            credential_type=credential_type,
        )

        credential_item.additional_properties = d
        return credential_item

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
