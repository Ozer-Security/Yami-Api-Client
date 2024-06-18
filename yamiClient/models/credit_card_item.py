from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar('T', bound='CreditCardItem')


@_attrs_define
class CreditCardItem:
    """
    Attributes:
        hwid (str):
        telegram (Union[None, str]):
        build_id (Union[None, str]):
        ip (Union[None, str]):
        leak_date (Union[None, str]):
        holder (Union[None, str]):
        card_type (Union[None, str]):
        card_number (Union[None, str]):
        expire_date (Union[None, str]):
    """

    hwid: str
    telegram: Union[None, str]
    build_id: Union[None, str]
    ip: Union[None, str]
    leak_date: Union[None, str]
    holder: Union[None, str]
    card_type: Union[None, str]
    card_number: Union[None, str]
    expire_date: Union[None, str]
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

        holder: Union[None, str]
        holder = self.holder

        card_type: Union[None, str]
        card_type = self.card_type

        card_number: Union[None, str]
        card_number = self.card_number

        expire_date: Union[None, str]
        expire_date = self.expire_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'hwid': hwid,
                'telegram': telegram,
                'buildId': build_id,
                'ip': ip,
                'leakDate': leak_date,
                'holder': holder,
                'cardType': card_type,
                'CardNumber': card_number,
                'expireDate': expire_date,
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

        def _parse_holder(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        holder = _parse_holder(d.pop('holder'))

        def _parse_card_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        card_type = _parse_card_type(d.pop('cardType'))

        def _parse_card_number(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        card_number = _parse_card_number(d.pop('CardNumber'))

        def _parse_expire_date(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        expire_date = _parse_expire_date(d.pop('expireDate'))

        credit_card_item = cls(
            hwid=hwid,
            telegram=telegram,
            build_id=build_id,
            ip=ip,
            leak_date=leak_date,
            holder=holder,
            card_type=card_type,
            card_number=card_number,
            expire_date=expire_date,
        )

        credit_card_item.additional_properties = d
        return credit_card_item

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
