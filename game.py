from dataclasses import dataclass
from matrix_struct import *
import random
import displayer
"""
this is the main game file that communicates with the user the handles the game logistics
"""

COLORS = ["#ffc700", "#7db954", "#fac4c4", "#ff284b", "#afddd5", "#ffb27b"]


@dataclass
class Game:
    player: str
    matrix: Matrix


def game_init() -> Game:
    """
    crates new game and initializes a game board for the user
    :return: created matrix
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
    # populate it
    matrix = populate(matrix)
    game = Game(user_name, matrix)
    return game


def populate(matrix: Matrix) -> Matrix:
    """
    populates the matrix with random colors
    :param matrix: the given matrix
    :return: populated matrix
    """

    for row in range(matrix.size):
        for col in range(matrix.size):
            sqr = get_sqr(row, col, matrix)
            sqr.content = get_color()

    # return the populated matrix
    return matrix


def get_color():
    """
    returns a randomly generated color from the COLORS list
    :return: color
    """
    num = random.randint(0, len(COLORS)-1)
    return COLORS[num]


def won(game: Game):
    """
    veryfies that all the colors are the same; in that case the player has won
    :param game: current game
    :return: True if all colors are the same:: False otherwise
    """
    # set current color to the first color found
    current_color = game.matrix.board[0][0].content

    for s1 in range(game.matrix.size):
        for s2 in range(game.matrix.size):
            if game.matrix.board[s1][s2] != current_color:
                return False
    return True


def main():
    game = game_init()
    displayer.init(game)


if __name__ == '__main__':
    main()