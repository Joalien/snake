def add_tuple(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


def distance_tuple(t1, t2):
    return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])


def is_illegal_move(snake, direction):
    return add_tuple(snake.direction.value, direction.value) == (0, 0)


def is_position_outside_board(board, position):
    return abs(position[0]) > board.size or abs(position[1]) > board.size


def is_position_inside_snake(snake, position):
    # Do not include last element
    return position in snake.position[:-1]


def losing_next_position(board, position):
    return is_position_inside_snake(board.snake, position) or is_position_outside_board(board, position)
