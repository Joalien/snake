import time
from typing import Tuple

import pygame
import threading

from Model.Board import Board
from View.OutputView.OutputView import OutputView

FACTOR = 50
border_size = FACTOR / 10
RECT_SIZE = (FACTOR - border_size, FACTOR - border_size)
SURFACE = pygame.Surface((FACTOR, FACTOR))
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
WHITE = pygame.Color(255, 255, 255)


class PygameOutputView(OutputView):
    def __init__(self, board_size: int):
        pygame.init()
        pygame.display.set_caption('Snake')
        board_size = board_size * 2 + 1
        self.gameDisplay = pygame.display.set_mode((board_size * FACTOR, board_size * FACTOR))
        threading.Thread(target=self.handle_events, daemon=True).start()

    def show_board(self, board: Board):
        self.gameDisplay.fill(WHITE)
        [self.draw_rect(GREEN, p, board.size) for p in board.snake.position]
        self.draw_rect(RED, board.food.position, board.size)
        pygame.display.update()

    def draw_rect(self, color: pygame.Color, position: Tuple[int, int], size: int):
        self.gameDisplay.fill(color, rect=(pygame.Rect(self.map_board_to_screen(position, size), RECT_SIZE)))

    @staticmethod
    def map_board_to_screen(position: Tuple[int, int], size: int) -> Tuple[float, float]:
        return (position[0] + size) * FACTOR + border_size / 2, (size - position[1]) * FACTOR + border_size / 2

    @staticmethod
    def handle_events():
        while True:
            time.sleep(1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    def send_message(self, message: int | str):
        print(message)
