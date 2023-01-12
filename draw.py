import numpy as np
from PIL import Image


class Canvas:
    """
    Creates the canvas on which the forms will be drawn and saves it
    to the file canvas.png
    """
    def __init__(self, width: int, height: int, color: list[int], filepath='canvas.png') -> None:
        self.width = width
        self.height = height
        self.color = color
        self.filepath = filepath
        self.array = np.zeros((self.height, self.width, 3), np.uint8)
        self.array[:] = [self.color[0], self.color[1], self.color[2]]

    def make(self) -> None:
        img = Image.fromarray(self.array, 'RGB')
        img.save(self.filepath)


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
