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


def update_board(game: Game, color: str):

    # start at the top left corner
    start_x = 0
    start_y = 0
    board = game.matrix.board

    matrix = check_adjacency(board[0][0], game.matrix, color)
    for row in game.matrix.board:
        print(row)
    print("updated")
    play(game)
    return


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


def check_adjacency(start: Square, matrix: Matrix, color: str):
    # queue where all the adjacencies are stored
    queue = []

    # add the start sqr, add color and activate
    queue.append(start)
    start.active = True
    start.color = color
    # update the matrix
    # matrix = update_sqr(matrix, start)
    turtle.speed(1)
    displayer.draw_square(start, matrix.size)

    while len(queue) != 0:
        curr_sqr = queue.pop(0)  # the current sqr to consider
        adj_list = gather_adj(matrix, curr_sqr)  # gather the adj

        # loop through the list of adjacencies
        for adj in adj_list:

            # inactive case
            if adj.active == False:
                # an inactive sqr may match the new color
                if adj.color == color:
                    # colors match, just activate
                    adj.active = True
                    # add to queue
                    queue.append(adj)

            else:  # if active
                if adj.color != color:
                    # change color
                    adj.color = color
                    # update on board
                    # matrix = update_sqr(matrix, adj)
                    # add it to the queue
                    displayer.draw_square(adj, matrix.size)
                    queue.append(adj)
    print("finish")
    return matrix


def accept_move(coord: tuple, game: Game):
    """
    accepts moves or 'clicks' from the user
    verifies if the coord of the click corresponds with a color
    :param coord: the coord of click from plater
    :param color_map: the list containing the color locations
    :return: color
    """
    turtle.onscreenclick(None)
    color_map = game.color_map
    color = ""
    for item in color_map:
        # if the x coord is within the first item
        if item.row < coord[0] < (item.row + displayer.SQR_SIZE):
            if (item.col - displayer.SQR_SIZE) < coord[1] < item.col:
                print("This is the color: ", item.color)
                color = item.color
                break
    update_board(game, color)
    print("out")



def play(game: Game):
    """
    this is where the game starts and takes user input
    :param game: the game being used
    :return: TODO
    """

    turtle.listen()
    turtle.onscreenclick(lambda x, y:
                         accept_move((x, y), game))





def main():
    game = game_init()
    game = displayer.init(game)

    # while not won(game):
    play(game)

    turtle.mainloop()


if __name__ == '__main__':
    main()
