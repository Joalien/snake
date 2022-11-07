from random import choice

from Model.Board import Board
from Model.Direction import Direction
from Strategy.Strategy import Strategy


class RandomStrategy(Strategy):
    def chose_next_move(self, board: Board) -> Direction:
        return choice(list(Direction))
