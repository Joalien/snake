import numpy as np
from numpy import ndarray

import utils
from Model.Board import Board
from utils import losing_next_position
from Model.Direction import Direction


def map_action_to_direction(current_direction: Direction, next_direction_index: int):
    return {
        0: current_direction.turn_left(),
        1: current_direction,
        2: current_direction.turn_right()
    }[next_direction_index]


def map_to_array(board: Board) -> ndarray[int]:
    # array = []
    # for j in range(board.size, -board.size - 1, -1):
    #     for i in range(-board.size, board.size + 1):
    #         if (i, j) == board.snake.head:
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
        board.food.position[1] > board.snake.head[1],
        board.food.position[1] < board.snake.head[1],
        board.food.position[0] > board.snake.head[0],
        board.food.position[0] < board.snake.head[0],
        losing_next_position(board, utils.add_tuple(board.snake.head, board.snake.direction.value)),
        losing_next_position(board, utils.add_tuple(board.snake.head, board.snake.direction.turn_left().value)),
        losing_next_position(board, utils.add_tuple(board.snake.head, board.snake.direction.turn_right().value)),
        board.snake.direction == Direction.UP,
        board.snake.direction == Direction.DOWN,
        board.snake.direction == Direction.RIGHT,
        board.snake.direction == Direction.LEFT
    ])))


