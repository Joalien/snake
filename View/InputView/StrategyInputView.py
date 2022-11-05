from View.InputView.InputView import InputView


class StrategyInputView(InputView):
    def __init__(self, strategy):
        self.strategy = strategy

    def get_input(self, board):
        return self.strategy.chose_next_move(board)
