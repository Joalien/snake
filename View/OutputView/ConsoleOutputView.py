from Model.Board import Board
from Model.Direction import Direction
from View.OutputView.OutputView import OutputView

SNAKE_HEAD = {
    Direction.UP: '^ ',
    Direction.RIGHT: '> ',
    Direction.DOWN: 'v ',
    Direction.LEFT: '< '
}
SNAKE_BODY = "x "
FOOD = 'o '
EMPTY_SQUARE = '. '


class ConsoleOutputView(OutputView):
    def show_board(self, board: Board):
        for j in range(board.size, -board.size - 1, -1):
            for i in range(-board.size, board.size + 1):
                if (i, j) == board.snake.head:
                    square = SNAKE_HEAD[board.snake.direction]
                elif (i, j) in board.snake.position:
                    square = SNAKE_BODY
                elif (i, j) == board.food.position:
                    square = FOOD
                else:
                    square = EMPTY_SQUARE
                print(square, end='')
            print()

    def send_message(self, message: int | str):
        print(message)
