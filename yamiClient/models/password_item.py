from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar('T', bound='PasswordItem')


@_attrs_define
class PasswordItem:
    """
    Attributes:
        hwid (str):
        telegram (Union[None, str]):
        build_id (Union[None, str]):
        ip (Union[None, str]):
        leak_date (Union[None, str]):
        username (Union[None, str]):
        password (Union[None, str]):
        url (Union[None, str]):
    """

    hwid: str
    telegram: Union[None, str]
    build_id: Union[None, str]
    ip: Union[None, str]
    leak_date: Union[None, str]
    username: Union[None, str]
    password: Union[None, str]
    url: Union[None, str]
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

        username: Union[None, str]
        username = self.username

        password: Union[None, str]
        password = self.password

        url: Union[None, str]
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'hwid': hwid,
                'telegram': telegram,
                'buildId': build_id,
                'ip': ip,
                'leakDate': leak_date,
                'username': username,
                'password': password,
                'url': url,
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

        def _parse_username(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        username = _parse_username(d.pop('username'))

        def _parse_password(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        password = _parse_password(d.pop('password'))

        def _parse_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        url = _parse_url(d.pop('url'))

        password_item = cls(
            hwid=hwid,
            telegram=telegram,
            build_id=build_id,
            ip=ip,
            leak_date=leak_date,
            username=username,
            password=password,
            url=url,
        )

        password_item.additional_properties = d
        return password_item

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
