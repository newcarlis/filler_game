import turtle

from matrix_struct import *
import displayer
"""
this is the main game file that communicates with the user the handles the game logistics
"""


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
    # create game
    game = Game(user_name, matrix)
    return game


def won(game: Game) -> bool:
    """
    veryfies that all the colors are the same; in that case the player has won
    :param game: current game
    :return: True if all colors are the same:: False otherwise
    """
    # set current color to the first color found
    current_color = game.matrix.board[0][0].color

    # check all the squares and their color
    for s1 in range(game.matrix.size):
        for s2 in range(game.matrix.size):
            if game.matrix.board[s1][s2].color != current_color:
                return False
    return True


def update_board(game: Game, color: str):

    # start at the bottom left corner

    # move in every direction and check if the colors match
    return False


def main():
    game = game_init()
    displayer.init(game)
    turtle.done()


if __name__ == '__main__':
    main()
