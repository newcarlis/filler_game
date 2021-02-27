"""
structure to represent the colored matrix used in the game
"""
import random
from dataclasses import dataclass
from typing import Any
# import game.displayer

COLORS = ["#ffc700", "#7db954", "#fac4c4", "#ff284b", "#afddd5", "#ffb27b"]

@dataclass
class ColorItem:
    row: float
    col: float
    color: str

@dataclass
class Square:
    """
    dataclass representing a single square on the board
    """
    row: int
    col: int
    color: str
    active: bool


@dataclass
class Matrix:
    """
    dataclass representing the entire board
    """
    size: int
    board: [['Square']]


def init_square(row: int, col: int, ) -> Square:
    """
    initialize a square with given coordinates and random colors
    :param row: x location
    :param col: y location
    :return: the created tile
    """

    sqr = Square(row, col, get_color(), False)

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

    matrix = Matrix(size, board)
    return matrix


def get_color():
    """
    returns a randomly generated color from the COLORS list
    :return: color
    """
    num = random.randint(0, len(COLORS)-1)
    return COLORS[num]


def get_sqr(row: int, col: int, matrix: Matrix) -> Square:
    """
    returns a square given its location on the matrix
    :param row: row of the square
    :param col: column location
    :param matrix: matrix containing the board
    :return: a square
    """

    return matrix.board[row][col]


def get_left(sqr: Square, matrix: Matrix) -> Square or None:
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


def get_right(sqr: Square, matrix: Matrix) -> Square or None:
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


def get_top(sqr: Square, matrix: Matrix) -> Square or None:
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


def get_bottom(sqr: Square, matrix: Matrix) -> Square or None:
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


def get_content(sqr: Square) -> Any:
    """
    gets content of the given square
    :param sqr: the square to consider
    :return: Square
    """
    return sqr.color


def update_sqr(matrix: Matrix, sqr: Square) -> Matrix:
    row = sqr.row
    col = sqr.col
    matrix.board[row][col] = sqr
    from game import displayer
    displayer.update_sqr(matrix, sqr)


    return matrix
