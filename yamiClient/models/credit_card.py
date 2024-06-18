from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar('T', bound='CreditCard')


@_attrs_define
class CreditCard:
    """
    Attributes:
        holder (Union[None, str]):
        card_type (Union[None, str]):
        card (Union[None, str]):
        expire_date (Union[None, str]):
        user_log_id (str):
        id (Union[Unset, str]):
    """

    holder: Union[None, str]
    card_type: Union[None, str]
    card: Union[None, str]
    expire_date: Union[None, str]
    user_log_id: str
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        holder: Union[None, str]
        holder = self.holder

        card_type: Union[None, str]
        card_type = self.card_type

        card: Union[None, str]
        card = self.card

        expire_date: Union[None, str]
        expire_date = self.expire_date

        user_log_id = self.user_log_id

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'holder': holder,
                'card_type': card_type,
                'card': card,
                'expire_date': expire_date,
                'user_log_id': user_log_id,
            }
        )
        if id is not UNSET:
            field_dict['id'] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_holder(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        holder = _parse_holder(d.pop('holder'))

        def _parse_card_type(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        card_type = _parse_card_type(d.pop('card_type'))

        def _parse_card(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        card = _parse_card(d.pop('card'))

        def _parse_expire_date(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        expire_date = _parse_expire_date(d.pop('expire_date'))

        user_log_id = d.pop('user_log_id')

        id = d.pop('id', UNSET)

        credit_card = cls(
            holder=holder,
            card_type=card_type,
            card=card,
            expire_date=expire_date,
            user_log_id=user_log_id,
            id=id,
        )

        credit_card.additional_properties = d
        return credit_card

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
