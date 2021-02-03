import turtle
from matrix_struct import *
"""
file that takes care of displaying game board 
"""

# each square in the game is expected to be 30 pixels
SQR_SIZE = 30
# padding space to compensate for space taken by window
PADDING = 50
# space between blocks and window margin
SPACE = 5

def init(matrix: Matrix):
    """
    initializes the game window to the necessary measurements
    :param matrix: the matrix representing the game
    :return: None
    """

    turtle.tracer(10, 10)

    # size the window so all blocks can fit
    width = (matrix.size * SQR_SIZE) + PADDING
    height = (matrix.size * SQR_SIZE) + PADDING

    # define the game window
    game_window = turtle.Screen()
    game_window.setup(width, height)

    # place the center of the screen in the bottom left
    game_window.setworldcoordinates(-SPACE, -SPACE, width, height)


    # loops trough the matrix board and draws each square
    for row in range(matrix.size):
        for col in range(matrix.size):
            draw_sqaure(matrix.board[row][col])

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
        turtle.forward(30)
        turtle.left(90)
    turtle.end_fill()

    # make sure to return to start position
    # turtle.goto(0, 0)

# test main function TODO: remove this
def main():
    matrix = init_matrix(10)
    init(matrix)
    turtle.mainloop()
    turtle.done()


main()



