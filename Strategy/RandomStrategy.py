from random import choice

from Model.Direction import Direction
from Strategy.Strategy import Strategy


class RandomStrategy(Strategy):
    def chose_next_move(self, board):
        return choice(list(Direction))
