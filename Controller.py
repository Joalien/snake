import utils
from Model.Board import Board
from Model.Direction import Direction
from Model.Snake import Snake
from Strategy.DQN.DQNStrategy import DQNStrategy
from View.InputView.StrategyInputView import StrategyInputView
from View.OutputView.PygameOutputView import *
from View.View import View
from utils import is_illegal_move, losing_next_position


def run(board_size=8):
    strategy = DQNStrategy()
    view = View(StrategyInputView(strategy), PygameOutputView(board_size))

    while True:
        board = Board(board_size, Snake((0, 0), Direction.UP))
        board.spawn_food()

        score = play_a_game(board, view)

        view.send_message(score)


def play_a_game(board, view, delay=0.05):
    while True:
        view.show_board(board)
        next_direction = get_next_legal_move(board, view)
        next_position = compute_next_position(board.snake, next_direction.value)
        if losing_next_position(board, next_position):
            view.send_message("You lose!")
            # TODO Can be improve
            rotate(board.snake, next_direction)
            move_forward(board.snake, next_position)
            view.show_board(board)
            return len(board.snake.position)

        rotate(board.snake, next_direction)
        move_forward(board.snake, next_position)

        if next_position == board.food.position:
            board.spawn_food()
        else:
            remove_last_position(board.snake)

        time.sleep(delay)


def get_next_legal_move(board, view):
    """
    :return: one value of the enum Direction
    """
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
    return utils.add_tuple(snake.head(), next_direction)


def rotate(snake, direction):
    snake.direction = direction


def lose():
    pass
