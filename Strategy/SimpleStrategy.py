from random import choice
from typing import Tuple

import utils
from Model.Board import Board
from Model.Direction import Direction
from Model.Snake import Snake
from Strategy.Strategy import Strategy


class SimpleStrategy(Strategy):
    def chose_next_move(self, board: Board) -> Direction:
        food_position = board.food.position
        head_position = board.snake.head
        distance = utils.distance_tuple(food_position, head_position)
        next_position = self.compute_next_position(board.snake, board.snake.direction)
        if utils.distance_tuple(food_position, next_position) <= distance:
            return board.snake.direction
        else:
            return choice(list(Direction))

    # FIXME duplicate
    @staticmethod
    def compute_next_position(snake: Snake, next_direction: Direction) -> Tuple:
        return utils.add_tuple(snake.head, next_direction.value)
