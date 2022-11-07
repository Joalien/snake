import utils
from Model.Direction import Direction
from Model.Snake import Snake
from Strategy.DQN.DQNStrategy import DQNStrategy
from View.InputView.InputView import InputView
from View.InputView.StrategyInputView import StrategyInputView
from View.OutputView.PygameOutputView import *
from utils import is_illegal_move, losing_next_position


def run(board_size=8):
    strategy = DQNStrategy()
    input_view, output_view = StrategyInputView(strategy), PygameOutputView(board_size)

    while True:
        board = Board(board_size, Snake((0, 0), Direction.UP))
        board.spawn_food()

        score: int | str = play_a_game(board, input_view, output_view)

        output_view.send_message(score)


def play_a_game(board: Board, input_view: InputView, output_view: OutputView, delay=0.05) -> int:
    while True:
        output_view.show_board(board)
        next_direction = get_next_legal_move(board, input_view)
        next_position = compute_next_position(board.snake, next_direction.value)
        if losing_next_position(board, next_position):
            output_view.send_message("You lose!")
            # TODO Can be improve
            rotate(board.snake, next_direction)
            move_forward(board.snake, next_position)
            output_view.show_board(board)
            return len(board.snake.position)

        rotate(board.snake, next_direction)
        move_forward(board.snake, next_position)

        if next_position == board.food.position:
            board.spawn_food()
        else:
            remove_last_position(board.snake)

        time.sleep(delay)


def get_next_legal_move(board: Board, view: InputView) -> Direction:
    """
    :return: one value of the enum Direction
    """
    next_direction = view.get_input(board)
    while is_illegal_move(board.snake, next_direction):
        next_direction = view.get_input(board)
    return next_direction


def remove_last_position(snake: Snake):
    snake.position.pop()


def move_forward(snake: Snake, next_position: Tuple[int, int]):
    snake.position.insert(0, next_position)


def compute_next_position(snake: Snake, next_direction: Tuple[int, int]) -> Tuple[int, int]:
    return utils.add_tuple(snake.head, next_direction)


def rotate(snake: Snake, direction: Direction):
    snake.direction = direction


def lose():
    pass
