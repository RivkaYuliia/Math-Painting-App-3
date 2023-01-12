import numpy as np


class Canvas:
    """
    Creates the canvas on which the forms will be drawn and saves it
    to the file canvas.png
    """
    def __init__(self, width: int, height: int, color: list[int]) -> None:
        self.width = width
        self.height = height
        self.color = color

    def make(self):
        pass


class Rectangle:
    """
    Draws forms such as rectangles or squares in the canvas file.
    """
    def __init__(self, x: int, y: int, width: int, height: int, color: list[int]) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pass


print("Hi! Let's create a canvas to draw something.")
canvas_w = int(input('What is the width of the canvas? '))
canvas_h = int(input('What is the height of the canvas? '))
canvas_color = list()
canvas_color.append(int(input('Now the color! How much red in the color (from 0 to 255)? ')))
canvas_color.append(int(input('How much green in the color (from 0 to 255)? ')))
canvas_color.append(int(input('How much blue in the color (from 0 to 255)? ')))
while True:
    form = input('What do you want to draw, a square or a rectangle? (type "Q" for exit) ')
    if form == 'Q':
        break
    x = int(input('Enter the X of the upper left point: '))
    y = int(input('Enter the Y of the upper left point: '))
    if form == 'square':
        width = height = int(input('Enter the side of the square: '))
    else:
        width = int(input('Enter the width of the rectangle: '))
        height = int(input('Enter the height of the rectangle: '))
    color = [
        int(input('Now the color! How much red in the color (from 0 to 255)? ')),
        int(input('How much green in the color (from 0 to 255)? ')),
        int(input('How much blue in the color (from 0 to 255)? '))
    ]

