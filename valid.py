class Validator:
    """
    Contains several methods for validation of user inputs, such as color and form
    """
    def __init__(self, user_input: str | int = None) -> None:
        self.user_input = user_input

    def canvas_color(self, user_input):
        self.user_input = user_input
        if self.user_input == 'w' or self.user_input == 'b':
            return self.user_input
        return False

    def form(self, user_input):
        self.user_input = user_input
        if self.user_input == 's' or self.user_input == 'r' or self.user_input == 'q':
            return self.user_input
        return False
