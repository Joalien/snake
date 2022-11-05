from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def chose_next_move(self, board):
        """
        Chose the next move to play
        :param board: the board containing snake, food and its size
        :return: best move regarding of the strategy
        """
        pass
