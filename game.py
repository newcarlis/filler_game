from dataclasses import dataclass
from matrix_struct import *
import random
"""
this is the main game file that communicates with the user the handles the game logistics
"""

COLORS = ["#ffc700", "#7db954", "#fac4c", "#ff284b", "#afddd5", "#ffb27b"]

def game_init():
    """
    crates new game and initializes a game board for the user
    :return: TODO: figure this out
    """

    # welcome the user and setup board size
    user_name = input("what is your name?\n")
    print("hi {fname} Welcome to the Filler Game!".format(fname = user_name))

    size = 0
    in_size = input("what size would you like the board to be?\na. 8x8\nb. 16x16\nc. 24x24\n")
    if in_size == 'a' or in_size == 'A':
        size = 8
    elif in_size == 'b' or in_size == 'B':
        size = 16
    elif in_size == 'c' or in_size == 'C':
        size = 24

    # create matrix
    matrix = init_matrix(size)


def populate(matrix: Matrix):
    """
    populates the matrix with random colors
    :param matrix: the given matrix
    :return: TODO
    """

    for col in range(matrix.board):
        for row in range(matrix.board):
            sqr = get_sqr(row, col, matrix)
            sqr.content = get_color()


def get_color():
    """
    returns a randomly generated color from the COLORS list
    :return: color
    """
    num = random.randint(0, len(COLORS))
    return COLORS[num]


def main():
    game_init()


if __name__ == '__main__':
    main()