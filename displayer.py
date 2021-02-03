import turtle
from matrix_struct import *
"""
file that takes care of displaying game board 
"""

# each block in the game is expected to be 30 pixels
BLOCK_SIZE = 30
# padding space to compensate for space taken by window
PADDING = 50
# space between blocks and window margin
SPACE = 10

def init(matrix: Matrix):
    """
    initializes the game window to the necessary measurements
    :param matrix: the matrix representing the game
    :return: None
    """

    # size the window so all blocks can fit
    width = (matrix.size * BLOCK_SIZE) + PADDING
    height = (matrix.size * BLOCK_SIZE) + PADDING

    # define the game window
    game_window = turtle.Screen()
    game_window.setup(width, height)

    # place the center of the screen in the bottom left
    game_window.setworldcoordinates(-SPACE, -SPACE, width, height)


# test main function
def main():
    matrix = init_matrix(4)
    turtle.speed(0)
    # print(matrix)
    init(matrix)
    turtle.done()


main()



