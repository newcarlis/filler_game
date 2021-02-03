"""
structure to represent a matrix based game.
contains functions for matrix creation and modification
"""
from dataclasses import dataclass
from typing import Any


@dataclass
class Square:
    """
    dataclass representing a single square on the board
    """
    row: int
    col: int
    content: Any

@dataclass
class Matrix:
    """
    dataclass representing the entire board
    """
    size: int
    board: [['Square']]


def init_Square(row: int, col: int, ) -> Square:
    """
    initialize a square with given coordinates and random colors
    :param row: x location
    :param col: y location
    :return: the created tile
    """
    sqr = Square(row, col, 'red')
    # print(row, "---", col)
    # print(sqr)
    return sqr


def init_matrix(size: int):
    """
    function to initialize a matrix with random tiles
    :param size: size to initialize matrix
    :param board: the board
    :return: the created matrix
    """
    board = []
    print(board)

    # initializing individual squares
    for row in range(size):
        sub = []
        for col in range(size):
            sub.append(init_Square(row,col))
        board.append(sub)

    matrix = Matrix(size, board)
    print(board)
    return matrix


def get_left(sqr: Square, matrix: Matrix) -> Square or None:
    """
    function to access the square to the left of the given Square
    :param sqr: the square on the matrix to consider
    :param matrix: the game matrix being used
    :return: square to the left
    """

    if sqr.row == 0:
        return None

    row = sqr.row - 1
    col = sqr.col
    return matrix.board[row][col]


def get_right(sqr: Square, matrix: Matrix) -> Square or None:
    """
    function to access the square to the right of the given Square
    :param sqr: the square on the matrix to consider
    :param matrix: the game matrix being used
    :return: square to the right
    """

    if sqr.row == matrix.size - 1:
        return None

    row = sqr.row + 1
    col = sqr.col
    return matrix.board[row][col]


def get_top(sqr: Square, matrix: Matrix) -> Square or None:
    """
    function to access the square above the given Square
    :param sqr: the square on the matrix to consider
    :param matrix: the game matrix being used
    :return: square above
    """

    if sqr.col == 0:
        return None

    row = sqr.row
    col = sqr.col - 1
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

    row = sqr.row
    col = sqr.col + 1
    return matrix.board[row][col]


def get_content(sqr: Square) -> Any:
    """
    gets content of the given square
    :param sqr: the square to consider
    :return: Square
    """
    return sqr.content

