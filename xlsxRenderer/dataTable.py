from dataclasses import dataclass
from enum import StrEnum
from typing import TypeVar


T = TypeVar('T', str, int, bool, float, bytes)


class ConditionnalFormatting(StrEnum):
    NONE = 'NONE'
    BINARY = 'BINARY'
    GRADIENT = 'GRADIENT'
    REVERSE_GRADIENT = 'REVERSE_GRADIENT'
    COLOR_CYCLE = 'COLOR_CYCLE'


@dataclass
class Header:
    position: int
    name: str
    htype: type[T]
    conditional_formatting: ConditionnalFormatting = ConditionnalFormatting.NONE


@dataclass
class DataTable:
    headers: list[Header]
    data: list[dict[str, T]]
