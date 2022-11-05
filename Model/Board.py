import random

from Model.Food import Food


class Board:
    def __init__(self, size, snake):
        self.size = size
        self.snake = snake
        self.food = None
        self.spawn_food()

    def spawn_food(self):
        x = random.randint(-self.size, self.size)
        y = random.randint(-self.size, self.size)
        if (x, y) in self.snake.position:
            self.spawn_food()
        else:
            self.food = Food((x, y))
