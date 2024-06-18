from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar('T', bound='NewUser')


@_attrs_define
class NewUser:
    """
    Attributes:
        main_domain (str):
        is_poc (bool):
        has_full_access (bool):
        public_key (str):
    """

    main_domain: str
    is_poc: bool
    has_full_access: bool
    public_key: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        main_domain = self.main_domain

        is_poc = self.is_poc

        has_full_access = self.has_full_access

        public_key = self.public_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'main_domain': main_domain,
                'is_poc': is_poc,
                'has_full_access': has_full_access,
                'public_key': public_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        main_domain = d.pop('main_domain')

        is_poc = d.pop('is_poc')

        has_full_access = d.pop('has_full_access')

        public_key = d.pop('public_key')

        new_user = cls(
            main_domain=main_domain,
            is_poc=is_poc,
            has_full_access=has_full_access,
            public_key=public_key,
        )

        new_user.additional_properties = d
        return new_user

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
