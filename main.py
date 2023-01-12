import numpy as np
from PIL import Image


class Canvas:
    """
    Creates the canvas on which the forms will be drawn and saves it
    to the file canvas.png
    """
    def __init__(self, width: int, height: int, color: list[int], filename='canvas.png', array=None) -> None:
        self.width = width
        self.height = height
        self.color = color
        self.array = array
        self.filename = filename

    def make(self) -> None:
        array = np.zeros((self.height, self.width, 3), np.uint8)
        array[:] = [self.color[0], self.color[1], self.color[2]]
        self.array = array


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

    def draw(self, canvas: Canvas):
        canvas.array[self.y:self.y+self.height, self.x:self.x+self.width] = self.color
        img = Image.fromarray(canvas.array, 'RGB')
        img.save(canvas.filename)


print("Hi! Let's create a canvas to draw something.")
canvas_w = int(input('What is the width of the canvas? '))
canvas_h = int(input('What is the height of the canvas? '))
user_color = input('What is the color of the canvas, white(w) or black(b)? ')
canvas_color = [255, 255, 255] if user_color == 'w' else [0, 0, 0]
while True:
    form = input('What do you want to draw, a square(s) or a rectangle(r)? (type "q" for exit) ')
    if form == 'q':
        break
    x = int(input('Enter the X of the upper left point: '))
    y = int(input('Enter the Y of the upper left point: '))
    if form == 's':
        width = height = int(input('Enter the side of the square: '))
    else:
        width = int(input('Enter the width of the rectangle: '))
        height = int(input('Enter the height of the rectangle: '))
    color = [
        int(input('Now the color! How much red in the color (from 0 to 255)? ')),
        int(input('How much green in the color (from 0 to 255)? ')),
        int(input('How much blue in the color (from 0 to 255)? '))
    ]

canvas = Canvas(canvas_w, canvas_h, canvas_color)
canvas.make()
rect = Rectangle(x, y, width, height, color)
rect.draw(canvas)
