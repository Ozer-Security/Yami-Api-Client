from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar('T', bound='LeakQueryResult')


@_attrs_define
class LeakQueryResult:
    """
    Attributes:
        email (str):
        database (str):
        leak_date (str):
        dataclasses (List[str]):
    """

    email: str
    database: str
    leak_date: Optional[str]
    dataclasses: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        database = self.database

        dataclasses = self.dataclasses

        leak_date = self.leak_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'email': email,
                'database': database,
                'leak_date': leak_date,
                'dataclasses': dataclasses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop('email')

        database = d.pop('database')

        leak_date = d.pop('leak_date')

        dataclasses = cast(List[str], d.pop('dataclasses'))

        leak_query_result = cls(
            email=email,
            database=database,
            leak_date=leak_date,
            dataclasses=dataclasses,
        )

        leak_query_result.additional_properties = d
        return leak_query_result

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
