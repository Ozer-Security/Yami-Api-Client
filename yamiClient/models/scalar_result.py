from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.leak_query_result import LeakQueryResult


T = TypeVar('T', bound='ScalarResult')


@_attrs_define
class ScalarResult:
    """
    Attributes:
        total_result_count (int):
        skip (int):
        limit (int):
        result (List['LeakQueryResult']):
    """

    total_result_count: int
    skip: int
    limit: int
    result: List['LeakQueryResult']
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_result_count = self.total_result_count

        skip = self.skip

        limit = self.limit

        result = []
        for result_item_data in self.result:
            result_item = result_item_data.to_dict()
            result.append(result_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                'total_result_count': total_result_count,
                'skip': skip,
                'limit': limit,
                'result': result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leak_query_result import LeakQueryResult

        d = src_dict.copy()
        total_result_count = d.pop('total_result_count')

        skip = d.pop('skip')

        limit = d.pop('limit')

        result = []
        _result = d.pop('result')
        for result_item_data in _result:
            result_item = LeakQueryResult.from_dict(result_item_data)

            result.append(result_item)

        scalar_result = cls(
            total_result_count=total_result_count,
            skip=skip,
            limit=limit,
            result=result,
        )

        scalar_result.additional_properties = d
        return scalar_result

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
