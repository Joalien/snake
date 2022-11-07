from abc import ABC, abstractmethod

from Model.Board import Board
from Model.Direction import Direction


class InputView(ABC):
    @abstractmethod
    def get_input(self, board: Board) -> Direction:
        """
        :return: direction wanted by user
        """
        pass
