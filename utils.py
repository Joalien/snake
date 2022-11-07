from typing import Tuple

from Model.Board import Board
from Model.Direction import Direction
from Model.Snake import Snake


def add_tuple(t1: Tuple[int, int], t2: Tuple[int, int]) -> Tuple[int, int]:
    return t1[0] + t2[0], t1[1] + t2[1]


def distance_tuple(t1: Tuple[int, int], t2: Tuple[int, int]) -> int:
    return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])


def is_illegal_move(snake: Snake, direction: Direction) -> bool:
    return add_tuple(snake.direction.value, direction.value) == (0, 0)


def is_position_outside_board(board: Board, position: Tuple[int, int]) -> bool:
    return abs(position[0]) > board.size or abs(position[1]) > board.size


def is_position_inside_snake(snake: Snake, position: Tuple[int, int]) -> bool:
    # Do not include last element
    return position in snake.position[:-1]


def losing_next_position(board: Board, position: Tuple[int, int]) -> bool:
    return is_position_inside_snake(board.snake, position) or is_position_outside_board(board, position)
