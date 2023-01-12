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
