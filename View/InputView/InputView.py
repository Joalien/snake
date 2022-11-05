from abc import ABC, abstractmethod


class InputView(ABC):
    @abstractmethod
    def get_input(self, board):
        """
        :return: direction wanted by user
        """
        pass
