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
    color_map: []


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
    game = Game(user_name, matrix, None)
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


def play(game: Game):
    """
    this is where the game starts and takes user input
    :param game: the game being used
    :return: TODO
    """
    turtle.onscreenclick(lambda x, y: displayer.accept_move((x, y), game))


def update_board(game: Game, color: str):

    # start at the top left corner
    start_x = 0
    start_y = 0
    board = game.matrix.board

    # traverse the matrix using the rows


    # return False

def gather_adj(matrix: Matrix, sqr: Square):
    adj = []  # list that will contain all of the adjacent squares

    # get the left adjacent square
    temp_sqr = get_left(sqr, matrix)
    if isinstance(temp_sqr, Square):
        adj.append(temp_sqr)

    # get the right adjacent square
    temp_sqr = get_right(sqr, matrix)
    if isinstance(temp_sqr, Square):
        adj.append(temp_sqr)

    # get the top adjacent square
    temp_sqr = get_top(sqr, matrix)
    if isinstance(temp_sqr, Square):
        adj.append(temp_sqr)

    # get the bottom adjacent square
    temp_sqr = get_bottom(sqr, matrix)
    if isinstance(temp_sqr, Square):
        adj.append(temp_sqr)

    return adj


def main():
    game = game_init()
    game = displayer.init(game)
    print(gather_adj(game.matrix, game.matrix.board[1][1]))
    # play(game)

    turtle.done()


if __name__ == '__main__':
    main()
