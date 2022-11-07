from abc import ABC, abstractmethod

from Model.Board import Board


class Strategy(ABC):
    @abstractmethod
    def chose_next_move(self, board: Board):
        """
        Chose the next move to play
        :param board: the board containing snake, food and its size
        :return: best move regarding of the strategy
        """
        pass
