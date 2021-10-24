from player import Player
from board import Board
from tile import Tile
from position import Position

TERMINAL = "TERMINAL"
WINDOW = "WINDOW"
options = ["exit", "terminal", "window"]

class Game:
    """
    class that manages the game and the logic
    as it is played.

    also prompts the user for the game mode

    attributes
    ----------
    player: Player
        object of the player using game
    size: int
        size of the game board
    """
    def __init__(self, size: int, player: Player):
        self.size = size
        self.board = Board(size)
        self.player = player

    @property
    def player(self) -> Player:
        return self._player
     
    @player.setter
    def player(self, player: Player):
        self._player = player

    def won(self) -> bool:
        """
        determines if games has finished and player won
        """
        color = self.board.get_tile(Position(0,0)).color

        for tile in self.board.__iter__():
            if tile.color != color:
                return False
        return True
