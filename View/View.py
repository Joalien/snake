class View:
    def __init__(self, input_view, output_view):
        self.input_view = input_view
        self.output_view = output_view

    def get_input(self, board):
        return self.input_view.get_input(board)

    def show_board(self, board):
        self.output_view.show_board(board)

    def send_message(self, message):
        self.output_view.send_message(message)
