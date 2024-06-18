from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar('T', bound='StolenFile')


@_attrs_define
class StolenFile:
    """
    Attributes:
        file_name (str):
        user_log_id (str):
        id (Union[Unset, str]):
    """

    file_name: str
    user_log_id: str
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        file_name = self.file_name

        user_log_id = self.user_log_id

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'file_name': file_name,
                'user_log_id': user_log_id,
            }
        )
        if id is not UNSET:
            field_dict['id'] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_name = d.pop('file_name')

        user_log_id = d.pop('user_log_id')

        id = d.pop('id', UNSET)

        stolen_file = cls(
            file_name=file_name,
            user_log_id=user_log_id,
            id=id,
        )

        stolen_file.additional_properties = d
        return stolen_file

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
