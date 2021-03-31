from tile import Tile
import numpy as np
from itertools import chain
from position import Position
from color import Color

class Board:
    """
    class that represents the board used in the game

    >> Attributes
    -------------
    size: int
        the size to give the board
    board: [[Tile]]
    2D array containing the tiles of the game
    """
    def __init__(self, size: int):
        self.size = size
        self.board = np.empty((size, size), dtype = Tile)

    @property
    def size(self) -> int:
        """
        getter for the size of the board
        """
        return self._size

    @size.setter
    def size(self, size: int) -> None:
        """
        setter for the size of the board
        
        params
        ------
        size: int
            size to set the board to
        """
        self._size = size

    @property
    def board(self) -> [[]]:
        """
        getter for the board
        """
        return self._board

    @board.setter
    def board(self, board) -> None:
        """
        setter for the board

        params
        ------
        board: [[Tile]]
            the new board to assign
        """
        self._board = board

    def pop_board(self) -> None:
        """
        populates the board with tiles
        """
        row = 0
        col = 0
        for tile in self.__iter__():
            pos = Position(row, col)
            self.board[row][col] = Tile(pos)
            if col == self.size - 1:
                row += 1
                col = 0
            else:       
                col += 1

    def get_up(self, pos) -> Tile:
        """
        returns the Tile above the given tile

        params
        ------
        pos: Position
            position of the given tile
        """
        if pos.x == 0:
            return None

        row = pos.x - 1
        col = pos.y
        return self.board[row][col]

    def get_down(self, pos) -> Tile:
        """
        returns the Tile below the given tile

        params
        ------
        pos: Position
            position of the given tile
        """
        if pos.x == self.size - 1:
            return None

        row = pos.x + 1
        col = pos.y
        return self.board[row][col]

    def get_left(self, pos) -> Tile:
        """
        returns the Tile next(left) to the given tile

        params
        ------
        pos: Position
            position of the given tile
        """
        if pos.y == 0:
            return None

        row = pos.x
        col = pos.y - 1
        return self.board[row][col]

    def get_right(self, pos) -> Tile:
        """
        returns the Tile next(right) to the given tile

        params
        ------
        pos: Position
            position of the given tile
        """
        if pos.y == self.size - 1:
            return None

        row = pos.x
        col = pos.y + 1
        return self.board[row][col]

    def get_next(tile: Tile) -> tuple:
        """
        gets the adjacent objects to the one given
        :param tile: object to find adjacents for
        """
        return (self.get_down(tile.pos), self.get_right(tile.pos))

    def __iter__(self) -> object:
        """
        returns iterable object of board
        """
        return chain.from_iterable(self.board)

    def __str__(self) -> str:
        """
        returns formal and interactive string
        representation of board
        """
        counter = 0
        str_builder = ""
        for tile in self.__iter__():
            if counter == self.size - 1:
                str_builder += repr(tile)
                str_builder += "\n"
                counter = 0
            else:
                str_builder += repr(tile)
                counter += 1
        return str_builder

    def __repr__(self) -> str:
        """
        returns informal representation 
        of board - non interactive
        for testing purposes
        """
        for tile in self.__iter__():
            print(tile)

b = Board(4)
b.pop_board()
print(repr(b))
