from dataclasses import dataclass
from enum import Enum
from typing import TypeVar


T = TypeVar('T', str, int, bool, float, bytes)


class ConditionnalFormatting(Enum):
    NONE = 0#'NONE'
    BINARY = 1#'BINARY'
    GRADIENT = 2#'GRADIENT'
    REVERSE_GRADIENT = 3#'REVERSE_GRADIENT'
    COLOR_CYCLE = 4#'COLOR_CYCLE'


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
