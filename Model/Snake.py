class Snake:
    def __init__(self, position, direction):
        """
        :param position: tuple (x, y)
        :param direction: direction
        """
        self.position = [position]
        self.direction = direction

    def head(self):
        return self.position[0]
