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
    # while validator.form(form) is False:
    #     form = input('Please enter the right form that is "square" or "rectangle" (s or r), or enter "q" for exit: ')
    if form == 'q':
        break
    x = int(validator.integer(input('Enter the X of the upper left point: ')))
    y = int(validator.integer(input('Enter the Y of the upper left point: ')))
    if form == 's':
        width = height = int(validator.integer(input('Enter the side of the square: ')))
    else:
        width = int(validator.integer(input('Enter the width of the rectangle: ')))
        height = int(validator.integer(input('Enter the height of the rectangle: ')))
    color = [
        int(validator.color(input('Now the color! How much red in the color (from 0 to 255)? '))),
        int(validator.color(input('How much green in the color (from 0 to 255)? '))),
        int(validator.color(input('How much blue in the color (from 0 to 255)? ')))
    ]

    rect = Rectangle(x, y, width, height, color)
    rect.draw(canvas)

canvas.make()

# Opens the result file with all the drawings that the user has made

webbrowser.open(canvas.filepath)
