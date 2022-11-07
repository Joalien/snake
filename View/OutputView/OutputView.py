from abc import ABC, abstractmethod

from Model.Board import Board


class OutputView(ABC):
    @abstractmethod
    def show_board(self, board: Board):
        pass

    @abstractmethod
    def send_message(self, message: int | str):
        pass
