import numpy as np

import utils
from utils import losing_next_position
from Model.Direction import Direction


def map_action_to_direction(current_direction, next_direction_index):
    return {
        0: Direction(turn_left(current_direction.value)),
        1: current_direction,
        2: Direction(turn_right(current_direction.value))
    }[next_direction_index]


def map_to_array(board):
    # array = []
    # for j in range(board.size, -board.size - 1, -1):
    #     for i in range(-board.size, board.size + 1):
    #         if (i, j) == board.snake.head():
    #             square = 3
    #         elif (i, j) in board.snake.position:
    #             square = 2
    #         elif (i, j) == board.food.position:
    #             square = -1
    #         else:
    #             square = 0
    #         array.append(square)
    # return np.array(array)

    # Apple above
    # Apple below
    # Apple right
    # Apple left
    # Danger in front of
    # Danger left
    # Danger right
    # Heading toward top
    # Heading toward below
    # Heading toward right
    # Heading toward left
    return np.array(list(map(int, [
        board.food.position[1] > board.snake.head()[1],
        board.food.position[1] < board.snake.head()[1],
        board.food.position[0] > board.snake.head()[0],
        board.food.position[0] < board.snake.head()[0],
        losing_next_position(board, utils.add_tuple(board.snake.head(), board.snake.direction.value)),
        losing_next_position(board, utils.add_tuple(board.snake.head(), turn_left(board.snake.direction.value))),
        losing_next_position(board, utils.add_tuple(board.snake.head(), turn_right(board.snake.direction.value))),
        board.snake.direction == Direction.UP,
        board.snake.direction == Direction.DOWN,
        board.snake.direction == Direction.RIGHT,
        board.snake.direction == Direction.LEFT
    ])))


def turn_right(origin):
    return origin[1], - origin[0]


def turn_left(origin):
    return - origin[1], origin[0]
