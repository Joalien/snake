from typing import Tuple, List

from Model.Direction import Direction


class Snake:
    def __init__(self, position: Tuple[int, int], direction: Direction):
        """
        :param position: tuple (x, y)
        :param direction: direction
        """
        self.position: List[Tuple[int, int]] = [position]
        self.direction: Direction = direction

    @property
    def head(self) -> Tuple[int, int]:
        return self.position[0]
