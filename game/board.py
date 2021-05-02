from tile import Tile
import tile
import numpy as np
from itertools import chain
from position import Position
from color import Color
from queue import Queue

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
        self.pop_board()
        self.vertical_span = tile.HEIGHT * self.size

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
        
        #activate relevant tiles
        self.set_actives()

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

    def get_next(self, tile: Tile) -> tuple:
        """
        gets the adjacent objects to the one given
        :param tile: object to find adjacents for
        """
        down = self.get_down(tile.pos)
        left = self.get_right(tile.pos)
        lst = []
        if(down is not None):
            lst.append(down)
        if(left is not None):
            lst.append(left)
        return lst

    def get_tile(self, pos: Position):
        return self.board[pos.x][pos.y]

    def set_actives(self) -> None:
        """
        when the game starts the initial tile might have
        adjacent ones of the same color, this ensures
        these are activated
        """
        tile = self.get_tile(Position(0,0))
        tile.active = True 
        color = tile.color
        self.update(color)

    def update(self, color: Color):
        """
        updates the board with the given color
        :param color: new color to update
        """
        # start at the top left corner
        start = self.get_tile(Position(0, 0))
        start.color = color

        # keep track of changes
        changes = 0 # TODO

        # set up a queue and put starting tile
        queue = Queue(maxsize = 3)
        queue.put(start)

        #BFS
        while not queue.empty():
            # deque top and get adjacents
            tile = queue.get()
            adjacents = self.get_next(tile)

            for next_tile in adjacents:
                if not next_tile.active:
                    # innactive tile might match the color
                    if next_tile.color == color:
                        #activate and add to queue
                        next_tile.active = True
                        queue.put(next_tile)

                else: # active case - change to match
                    if next_tile.color != color:
                        next_tile.color = color
                        #add to queue
                        queue.put(next_tile)

    def __iter__(self) -> object:
        """
        returns iterable object of board
        """
        return chain.from_iterable(self.board)

    def __str__(self) -> str:
        """
        returns informal representation 
        of board - non interactive
        for testing purposes
        """
        builder = ""
        for tile in self.__iter__():
            builder += str(tile) + "\n"

        return builder

    def __repr__(self) -> str:
        """
        returns formal and interactive string
        representation of board
        """
        counter = 0
        str_builder = ""
        line = ""
        for tile in self.__iter__():
            if counter == self.size - 1:
                line += repr(tile)
                line += "\n"
                str_builder += (line*2)
                line = ""
                counter = 0
            else:
                line += repr(tile)
                counter += 1
        return str_builder