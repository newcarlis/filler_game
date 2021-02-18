import turtle
from matrix_struct import *
from game import *
"""
file that takes care of displaying game board 
"""

# each square in the game is expected to be 30 pixels
SQR_SIZE = 30
# padding space to compensate for space taken by window
PADDING = 20
# space between blocks and window margin (Horizontally)
H_OFFSET = -5
# space between blocks and window margin (Vertical)
V_OFFSET = -15
# space taken by the color menu
COLOR_SPACE = 100
# this how much space the player info section is going to take

def init(game: Game):
    """
    initializes the game window to the necessary measurements
    :param matrix: the matrix representing the game
    :return: None
    """
    matrix = game.matrix
    turtle.tracer(50, 50)

    # size the window so all blocks can fit
    width = (matrix.size * SQR_SIZE) + PADDING
    height = (matrix.size * SQR_SIZE) + PADDING

    print("width: ", width, "\nheight: ", height, "\nspace for squares: ", matrix.size * SQR_SIZE)

    turtle.bgcolor('#9d9d9d')

    # turtle.setworldcoordinates(-10, -50, width, height - 50)
    turtle.Screen().setup(width,height)
    turtle.Screen().setworldcoordinates(H_OFFSET, V_OFFSET, width + H_OFFSET, height + V_OFFSET)

    turtle.hideturtle()

    # loops trough the matrix board and draws each square
    for row in range(matrix.size):
        for col in range(matrix.size):
            draw_sqaure(matrix.board[row][col])

    # turtle.up()
    # turtle.goto(0, (matrix.size * SQR_SIZE) + 5)
    # turtle.color("black")
    # turtle.write(game.player, font=("Courier", 25, 'normal'))

    turtle.up()
    # color_menu(matrix)

    turtle.done()

def draw_sqaure(sqr: Square):
    """
    used the information associated with the square to draw it on the board
    :param sqr: the square to be drawn
    :return: TODO: return type
    """

    turtle.up()
    turtle.goto(sqr.row * SQR_SIZE, sqr.col * SQR_SIZE)

    # code to draw a square
    # make sure the turtle is pointing east
    # turtle.setheading(0)

    # set the color
    turtle.color(sqr.content)
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(SQR_SIZE)
        turtle.left(90)
    turtle.end_fill()


def color_menu(matrix: Matrix):
    # this determines where to place the color blocks so they are evenly spaced
    color_spacing = ((matrix.size * SQR_SIZE) - (len(COLORS) * SQR_SIZE)) / (len(COLORS) - 1)
    print(color_spacing)
    turtle.goto((matrix.size * SQR_SIZE + 20), matrix.size * SQR_SIZE)

    turtle.setheading(270)

    for color in COLORS:
        turtle.color('black', color)
        turtle.down()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(SQR_SIZE)
            turtle.left(90)
        turtle.end_fill()

        turtle.up()
        turtle.forward(color_spacing + SQR_SIZE)

# test main function TODO: remove this
# def main():
#     matrix = init_matrix(10)
#     init(matrix)
#     turtle.mainloop()
#     turtle.done()
#
#
# main()



