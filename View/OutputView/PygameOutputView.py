import pygame

from View.OutputView.OutputView import OutputView

FACTOR = 50
RECT_SIZE = (FACTOR, FACTOR)
SURFACE = pygame.Surface((FACTOR, FACTOR))
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
WHITE = pygame.Color(255, 255, 255)


class PygameOutputView(OutputView):
    def __init__(self, board_size):
        pygame.init()
        pygame.display.set_caption('Snake')
        board_size = board_size * 2 + 1
        self.gameDisplay = pygame.display.set_mode((board_size * FACTOR, board_size * FACTOR))

    def show_board(self, board):
        self.gameDisplay.fill(WHITE)
        self.draw_rect(RED, board.food.position, board.size)
        [self.draw_rect(GREEN, p, board.size) for p in board.snake.position]
        pygame.display.update()

    def draw_rect(self, color, position, size):
        self.gameDisplay.fill(color, rect=(pygame.Rect(self.map_board_to_screen(position, size), RECT_SIZE)))

    @staticmethod
    def map_board_to_screen(position, size):
        return (position[0] + size) * FACTOR, (size - position[1]) * FACTOR

    def send_message(self, message):
        print(message)