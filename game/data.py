"""
structure to represent the colored matrix used in the game
"""

import random
from dataclasses import dataclass

#bg color of the window
BG_COLOR = '#9d9d9d'
# each square in the game is expected to be 30 pixels
SQR_SIZE = 30
# padding space to compensate for space taken by window
PADDING = 20
# space between blocks and window margin (Horizontally)
H_OFFSET = -5
# space between blocks and window margin (Vertical)
V_OFFSET = -15
"""
space taken by the color menu
This equates to SQR_SIZE of the colored boxes and the rest is padding
"""
COLOR_SPACE = 50
# this how much space the player info section is going to take
INFO_SPACE = 25
# info space padding
INFO_PADD = 5
# helps set location for the # of moves
INFO_PADD_2 = -100


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


@dataclass
class Player:
    name: str
    moves: int


@dataclass
class Game:
    player: Player
    matrix: Matrix
    color_map: []


def get_color():
    """
    returns a randomly generated color from the COLORS list
    :return: color
    """
    num = random.randint(0, len(COLORS)-1)
    return COLORS[num]
