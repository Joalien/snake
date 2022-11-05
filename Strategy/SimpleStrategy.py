from random import choice

import utils
from Model.Direction import Direction
from Strategy.Strategy import Strategy


class SimpleStrategy(Strategy):
    def chose_next_move(self, board):
        food_position = board.food.position
        head_position = board.snake.head()
        distance = utils.distance_tuple(food_position, head_position)
        next_position = self.compute_next_position(board.snake, board.snake.direction)
        if utils.distance_tuple(food_position, next_position) <= distance:
            return board.snake.direction
        else:
            return choice(list(Direction))

    @staticmethod
    def compute_next_position(snake, next_direction):
        return utils.add_tuple(snake.head(), next_direction.value)
