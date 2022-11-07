from Model.Board import Board
from Model.Direction import Direction
from Strategy.Strategy import Strategy
from View.InputView.InputView import InputView


class StrategyInputView(InputView):
    def __init__(self, strategy: Strategy):
        self.strategy: Strategy = strategy

    def get_input(self, board: Board) -> Direction:
        return self.strategy.chose_next_move(board)
