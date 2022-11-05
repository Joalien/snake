from abc import ABC, abstractmethod


class OutputView(ABC):
    @abstractmethod
    def show_board(self, board):
        pass

    @abstractmethod
    def send_message(self, message):
        pass
