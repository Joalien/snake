import time

import utils
from Model.Board import Board
from Model.Direction import Direction
from Model.Snake import Snake
from Strategy.SimpleStrategy import SimpleStrategy
from View.InputView.StrategyInputView import StrategyInputView
from View.OutputView.PygameOutputView import *
from View.View import View


def run():
    board_size = 5
    strategy = SimpleStrategy()
    view = View(StrategyInputView(strategy), PygameOutputView(board_size))

    while True:
        board = Board(board_size, Snake((0, 0), Direction.UP))
        board.spawn_food()

        score = play_a_game(board, view)

        view.send_message(score)


def play_a_game(board, view):
    while True:
        view.show_board(board)
        next_direction = get_next_legal_move(board, view)
        next_position = compute_next_position(board.snake, next_direction.value)
        if losing_next_position(board, next_position):
            view.send_message("You lose!")
            return len(board.snake.position)

        rotate(board.snake, next_direction)
        move_forward(board.snake, next_position)

        if next_position == board.food.position:
            board.spawn_food()
        else:
            remove_last_position(board.snake)

        time.sleep(0.05)


def get_next_legal_move(board, view):
    next_direction = view.get_input(board)
    while is_illegal_move(board.snake, next_direction):
        view.send_message('invalid move')
        next_direction = view.get_input(board)
    return next_direction


def remove_last_position(snake):
    snake.position.pop()


def move_forward(snake, next_position):
    snake.position.insert(0, next_position)


def compute_next_position(snake, next_direction):
    return utils.add_tuple(snake.position[0], next_direction)


def rotate(snake, direction):
    snake.direction = direction


def is_illegal_move(snake, direction):
    return utils.add_tuple(snake.direction.value, direction.value) == (0, 0)


def is_position_outside_board(board, position):
    return abs(position[0]) > board.size or abs(position[1]) > board.size


def is_position_inside_snake(snake, position):
    # Do not include last element
    return position in snake.position[:-1]


def losing_next_position(board, position):
    return is_position_inside_snake(board.snake, position) or is_position_outside_board(board, position)


def lose():
    pass
