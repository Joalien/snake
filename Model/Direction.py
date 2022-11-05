from enum import Enum


class Direction(Enum):
    UP = (0, 1)
    RIGHT = (1, 0)
    DOWN = (0, -1)
    LEFT = (-1, 0)


def find_from_value(value):
    for d in Direction:
        if d.value == value:
            return d
