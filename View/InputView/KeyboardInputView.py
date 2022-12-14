from Model.Direction import Direction
from View.InputView.InputView import InputView

KEY_MAPPING: dict[str, Direction] = {
    'z': Direction.UP,
    'd': Direction.RIGHT,
    's': Direction.DOWN,
    'q': Direction.LEFT
}


class KeyboardInputView(InputView):
    def get_input(self, _) -> Direction:
        next_direction = input()
        while next_direction not in KEY_MAPPING:
            next_direction = input()
        return KEY_MAPPING[next_direction]
