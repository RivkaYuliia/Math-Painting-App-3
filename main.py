from draw import Canvas, Rectangle
import valid
import webbrowser

validator = valid.Validator()  # We will use it to validate the user's inputs

# Creates canvas

print("Hi! Let's create a canvas to draw something.")
canvas_w = int(validator.integer(input('What is the width of the canvas? ')))
canvas_h = int(validator.integer(input('What is the height of the canvas? ')))
user_color = validator.canvas_color(input('What is the color of the canvas, white(w) or black(b)? '))
canvas_color = [255, 255, 255] if user_color == 'w' else [0, 0, 0]
canvas = Canvas(canvas_w, canvas_h, canvas_color)

# Main loop for drawing squares and rectangles

while True:
    form = validator.form(input('What do you want to draw, a square(s) or a rectangle(r)? (enter "q" for exit): '))
    if form == 'q':
        break
    x = int(validator.integer(input('Enter the X of the upper left point: ')))
    y = int(validator.integer(input('Enter the Y of the upper left point: ')))
    if form == 's':
        width = height = int(validator.integer(input('Enter the side of the square: ')))
    else:
        width = int(validator.integer(input('Enter the width of the rectangle: ')))
        height = int(validator.integer(input('Enter the height of the rectangle: ')))
    color = list()
    for i in ('red', 'green', 'blue'):
        color.append(int(validator.color(input(f'How much {i} in the color (from 0 to 255)? '))))

    rect = Rectangle(x, y, width, height, color)    # Creates a rectangle or a square and adds it to the canvas array
    rect.draw(canvas)

canvas.make()    # Writes all the drawing to the canvas file

webbrowser.open(canvas.filepath)    # Opens the result file with all the drawings that the user has made
