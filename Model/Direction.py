from __future__ import annotations

from enum import Enum
from types import DynamicClassAttribute
from typing import Tuple


class Direction(Enum):
    UP = (0, 1)
    RIGHT = (1, 0)
    DOWN = (0, -1)
    LEFT = (-1, 0)

    def turn_right(self) -> Direction:
        return Direction((self.value[1], - self.value[0]))

    def turn_left(self) -> Direction:
        return Direction((- self.value[1], self.value[0]))

    @DynamicClassAttribute
    def value(self) -> Tuple[int, int]:
        return self._value_
