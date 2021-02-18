import turtle
from matrix_struct import *
from game import *
"""
file that takes care of displaying game board 
"""

# each square in the game is expected to be 30 pixels
SQR_SIZE = 20
# padding space to compensate for space taken by window
PADDING = 20
# space between blocks and window margin (Horizontally)
H_OFFSET = -5
# space between blocks and window margin (Vertical)
V_OFFSET = -15
"""
space taken by the color menu
This equates to SQR_SIZE of the colored boxes and the rest is padding
"""
COLOR_SPACE = 50
# this how much space the player info section is going to take
INFO_SPACE = 25
# info space padding
INFO_PADD = 5
# helps set location for the # of moves
INFO_PADD_2 = -100


def init(game: Game):
    """
    initializes the game window to the necessary measurements
    :param matrix: the matrix representing the game
    :return: None
    """
    # matrix in use during the game
    matrix = game.matrix
    # makes the turtle draw everything before displaying
    turtle.tracer(50, 50)

    # size the window so all elements can fit
    width = (matrix.size * SQR_SIZE) + PADDING + COLOR_SPACE
    height = (matrix.size * SQR_SIZE) + PADDING + INFO_SPACE

    # background color | Dark gray
    turtle.bgcolor('#9d9d9d')

    # sets up the world and appropriately sizes the window
    turtle.Screen().setup(width, height)
    turtle.Screen().setworldcoordinates(H_OFFSET, V_OFFSET, width + H_OFFSET, height + V_OFFSET)

    # hide turtle before drawing
    turtle.hideturtle()

    # loops trough the matrix board and draws each square
    for row in range(matrix.size):
        for col in range(matrix.size):
            draw_sqaure(matrix.board[row][col])

    # draw the player info section
    turtle.up()
    # go above matrix
    turtle.goto(0, (matrix.size * SQR_SIZE) + INFO_PADD)
    turtle.color("black")
    turtle.write(game.player, font=("Courier", 12, 'normal'))

    # draw the moves display
    set_moves(matrix)

    turtle.up()
    color_menu(matrix)


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
    turtle.color(sqr.color)
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(SQR_SIZE)
        turtle.left(90)
    turtle.end_fill()

def set_moves(matrix: Matrix):
    """
    updates the number of moves as the player plays.
    :param matrix: the current matrix being used
    :return: NONE
    """
    # go to the position where moves are displayed
    turtle.goto((matrix.size * SQR_SIZE) + INFO_PADD_2, (matrix.size * SQR_SIZE) + INFO_PADD)
    turtle.color("black")
    turtle.write("Moves: 200", font=("Courier", 12, 'normal'))

def color_menu(matrix: Matrix):
    """
    Creates the color menu to the right of the board.
    equally spaces the colors so it looks neat
    :param matrix: the current matrix used
    :return: NONE
    """
    # this determines where to place the color blocks so they are evenly spaced
    color_spacing = ((matrix.size * SQR_SIZE) - (len(COLORS) * SQR_SIZE)) / (len(COLORS) - 1)
    padding = (COLOR_SPACE - SQR_SIZE) / 2
    turtle.goto((matrix.size * SQR_SIZE + padding), matrix.size * SQR_SIZE)

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


def generate_coords(x: int, y: int) -> tuple:
    """
    this generates coordinates. The coordinates are given by a click on the canvas,
    and they are returned as a tuple for further use
    :param x: x coord of click
    :param y: y coord of click
    :return: tuple(x,y)
    """
    return x, y


def check(x, y):
    turtle.bgcolor("red")
    print("this is x: ", x, "this is y: ", y)




