from tile import Tile
import numpy as np
from itertools import chain

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

    def __iter__(self):
        return chain.from_iterable(self.board)

    def __str__(self):
        counter = 0
        str_builder = ""
        for tile in self.__iter__():
            if counter == self.size:
                str_builder += "\n"
                str_builder += repr(tile) + " "
                counter = 0
            else:
                str_builder += repr(tile) + " "
                counter += 1
        return str_builder

b= Board(2)
print(b)