import turtle

import data
import displayer
import setup
"""
main program file, handles the logic of the game main user interaction
"""


def get_left(sqr: data.Square, matrix: data.Matrix) -> data.Square or None:
    """
    function to access the square to the left of the given Square
    :param sqr: the square on the matrix to consider
    :param matrix: the game matrix being used
    :return: square to the left
    """

    if sqr.col == 0:
        return None

    row = sqr.row
    col = sqr.col - 1
    return matrix.board[row][col]


def get_right(sqr: data.Square, matrix: data.Matrix) -> data.Square or None:
    """
    function to access the square to the right of the given Square
    :param sqr: the square on the matrix to consider
    :param matrix: the game matrix being used
    :return: square to the right
    """

    if sqr.col == matrix.size - 1:
        return None

    row = sqr.row
    col = sqr.col + 1
    return matrix.board[row][col]


def get_top(sqr: data.Square, matrix: data.Matrix) -> data.Square or None:
    """
    function to access the square above the given Square
    :param sqr: the square on the matrix to consider
    :param matrix: the game matrix being used
    :return: square above
    """

    if sqr.row == 0:
        return None

    row = sqr.row - 1
    col = sqr.col
    return matrix.board[row][col]


def get_bottom(sqr: data.Square, matrix: data.Matrix) -> data.Square or None:
    """
    function to access the square bellow the given Square
    :param sqr: the square on the matrix to consider
    :param matrix: the game matrix being used
    :return: square below
    """

    if sqr.row == matrix.size - 1:
        return None

    row = sqr.row + 1
    col = sqr.col
    return matrix.board[row][col]


def won(game: data.Game) -> bool:
    """
    checks if the player has won
    :param game: the current game
    :return: true-> player has won; false-> not won
    """

    # color to use as reference
    current_color = game.matrix.board[0][0].color

    # all colors should match
    for s1 in range(game.matrix.size):
        for s2 in range(game.matrix.size):
            if game.matrix.board[s1][s2].color != current_color:
                return False
    return True


def update_board(game: data.Game, color: str):
    """
    updates the board with the given color
    :param game: current game
    :param color: new color to update
    :return: None
    """
    # start at the top left corner
    matrix = game.matrix
    start = matrix.board[0][0]
    check_adjacency(start, game.matrix, color)

    # continue playing
    play(game)
    return


def gather_adj(matrix: data.Matrix, sqr: data.Square):
    """
    gahters the adjacent squares to the one given
    :param matrix: current game matrix
    :param sqr: current square
    :return: list of adjacencies
    """
    adj = []

    # get the left adjacent square
    temp_sqr = get_left(sqr, matrix)
    if isinstance(temp_sqr, data.Square):
        adj.append(temp_sqr)

    # get the right adjacent square
    temp_sqr = get_right(sqr, matrix)
    if isinstance(temp_sqr, data.Square):
        adj.append(temp_sqr)

    # get the top adjacent square
    temp_sqr = get_top(sqr, matrix)
    if isinstance(temp_sqr, data.Square):
        adj.append(temp_sqr)

    # get the bottom adjacent square
    temp_sqr = get_bottom(sqr, matrix)
    if isinstance(temp_sqr, data.Square):
        adj.append(temp_sqr)

    return adj


def check_adjacency(start: data.Square, matrix: data.Matrix, color: str):
    """
    treats the game board as a graph ans performs a BFS algorithm to check
    and update all adjacent squares
    @pre: start at top left square (0, 0)
    :param start: starting position(square)
    :param matrix: current matrix
    :param color: color to update
    :return: None
    """

    # queue where all the search nodes are stored
    queue = []

    # add the start sqr, add color and activate
    queue.append(start)
    start.active = True
    start.color = color
    # update the matrix
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
                    # add it to the queue
                    displayer.draw_square(adj, matrix.size)
                    queue.append(adj)
    return matrix


def accept_move(coord: tuple, game: data.Game):
    """
    accepts moves or 'clicks' from the user
    checks if the coord of the click corresponds with a color
    :post: update the board if color found
    :param coord: the coord of click from plater
    :param game: current game session
    :return: None
    """
    displayer.toggle_screen_click(False, game)
    # reflect a new move on the player and the board
    game.player.moves += 1
    displayer.set_moves(game)
    color_map = game.color_map
    color = ""
    for item in color_map:
        # if the x coord is within the first item
        if item.row < coord[0] < (item.row + data.SQR_SIZE):
            if (item.col - data.SQR_SIZE) < coord[1] < item.col:
                color = item.color
                break
    update_board(game, color)


def play(game: data.Game):
    """
    this is where the game starts and takes user input
    :param game: the game being used
    :return: None
    """

    if not won(game):
        displayer.toggle_screen_click(True, game)
    else:
        print("you won!!")

def com():
    """
    handles initial communication with the user.
    :return:
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
        size = 20

    return data.Player(user_name, 0), size


def main():
    com_data = com()
    matrix = setup.init_matrix(com_data[1])
    game = setup.init_game(com_data[0], matrix)
    displayer.init_win(game)
    play(game)

    turtle.mainloop()
if __name__ == '__main__':
    main()
