import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar('T', bound='UserBase')


@_attrs_define
class UserBase:
    """
    Attributes:
        main_domain (str):
        is_valid_until (datetime.datetime):
        public_key (str):
        id (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
        is_superuser (Union[Unset, bool]):  Default: False.
        is_poc (Union[Unset, bool]):  Default: True.
        has_full_access (Union[Unset, bool]):  Default: False.
    """

    main_domain: str
    is_valid_until: datetime.datetime
    public_key: str
    id: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    is_superuser: Union[Unset, bool] = False
    is_poc: Union[Unset, bool] = True
    has_full_access: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        main_domain = self.main_domain

        is_valid_until = self.is_valid_until.isoformat()

        public_key = self.public_key

        id = self.id

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        is_superuser = self.is_superuser

        is_poc = self.is_poc

        has_full_access = self.has_full_access

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'main_domain': main_domain,
                'is_valid_until': is_valid_until,
                'public_key': public_key,
            }
        )
        if id is not UNSET:
            field_dict['id'] = id
        if created_at is not UNSET:
            field_dict['created_at'] = created_at
        if updated_at is not UNSET:
            field_dict['updated_at'] = updated_at
        if is_superuser is not UNSET:
            field_dict['is_superuser'] = is_superuser
        if is_poc is not UNSET:
            field_dict['is_poc'] = is_poc
        if has_full_access is not UNSET:
            field_dict['has_full_access'] = has_full_access

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        main_domain = d.pop('main_domain')

        is_valid_until = isoparse(d.pop('is_valid_until'))

        public_key = d.pop('public_key')

        id = d.pop('id', UNSET)

        _created_at = d.pop('created_at', UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop('updated_at', UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        is_superuser = d.pop('is_superuser', UNSET)

        is_poc = d.pop('is_poc', UNSET)

        has_full_access = d.pop('has_full_access', UNSET)

        user_base = cls(
            main_domain=main_domain,
            is_valid_until=is_valid_until,
            public_key=public_key,
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            is_superuser=is_superuser,
            is_poc=is_poc,
            has_full_access=has_full_access,
        )

        user_base.additional_properties = d
        return user_base

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
