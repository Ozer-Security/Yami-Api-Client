from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar('T', bound='UserLog')


@_attrs_define
class UserLog:
    """
    Attributes:
        hwid (str):
        telegram (Union[None, str]):
        build_id (Union[None, str]):
        ip (Union[None, str]):
        date (Union[None, str]):
        id (Union[Unset, str]):
    """

    hwid: str
    telegram: Union[None, str]
    build_id: Union[None, str]
    ip: Union[None, str]
    date: Union[None, str]
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hwid = self.hwid

        telegram: Union[None, str]
        telegram = self.telegram

        build_id: Union[None, str]
        build_id = self.build_id

        ip: Union[None, str]
        ip = self.ip

        date: Union[None, str]
        date = self.date

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'hwid': hwid,
                'telegram': telegram,
                'build_id': build_id,
                'ip': ip,
                'date': date,
            }
        )
        if id is not UNSET:
            field_dict['id'] = id

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

        build_id = _parse_build_id(d.pop('build_id'))

        def _parse_ip(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        ip = _parse_ip(d.pop('ip'))

        def _parse_date(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        date = _parse_date(d.pop('date'))

        id = d.pop('id', UNSET)

        user_log = cls(
            hwid=hwid,
            telegram=telegram,
            build_id=build_id,
            ip=ip,
            date=date,
            id=id,
        )

        user_log.additional_properties = d
        return user_log

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
