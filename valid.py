class Validator:
    """
    Contains several methods for validation of user inputs, such as color and form
    """
    @staticmethod
    def canvas_color(user_input: str) -> str:
        while True:
            if user_input == 'w' or user_input == 'b':
                break
            else:
                user_input = input('The color can be either white or black (w or b). Enter the right letter please: ')
        return user_input

    @staticmethod
    def form(user_input: str) -> str:
        while True:
            if user_input == 's' or user_input == 'r' or user_input == 'q':
                break
            else:
                user_input = input('Please enter the right form that is "square" or "rectangle" (s or r), or '
                                   'enter "q" for exit: ')
        return user_input

    @staticmethod
    def integer(user_input: str) -> str:
        while True:
            if user_input.isdigit():
                break
            else:
                user_input = input('Enter a positive integer, please: ')
        return user_input

    @staticmethod
    def color(user_input: str) -> str:
        while True:
            if user_input.isdigit() and 0 <= int(user_input) <= 255:
                break
            else:
                user_input = input('Enter a positive integer from 0 up to 255, please: ')
        return user_input
