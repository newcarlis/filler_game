import data


def init_game(player: data.Player, matrix: data.Matrix) -> data.Game:
    """
    crates new game and initializes a game board for the user
    :return: created matrix
    """
    game = data.Game(player, matrix, [])
    return game


def init_square(row: int, col: int, ) -> data.Square:
    """
    initialize a square with given coordinates and random colors
    :param row: x location
    :param col: y location
    :return: the created tile
    """

    sqr = data.Square(row, col, data.get_color(), False)

    return sqr


def init_matrix(size: int):
    """
    function to initialize a matrix with random squares
    :param size: size to initialize matrix
    :return: the created matrix
    """
    board = []

    # initializing individual squares
    for row in range(size):
        sub = []
        for col in range(size):
            sub.append(init_square(row, col))
        board.append(sub)

    matrix = data.Matrix(size, board)
    return matrix

