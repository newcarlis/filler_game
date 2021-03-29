from tile import Tile
import numpy as np
from itertools import chain
from position import Position

class Board:

    def __init__(self, size):
        self.size = size
        self.board = np.empty((size, size), dtype = Tile)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board

    def pop_board(self):
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
            
            

    def __iter__(self):
        return chain.from_iterable(self.board)

    def __str__(self):
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

    def __repr__(self):
        for tile in self.__iter__():
            print(tile)
