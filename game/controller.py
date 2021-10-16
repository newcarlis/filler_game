import sys
from color import Color
import color
from player import Player
from board import Board
from tile import Tile
from position import Position
import time
import re
from sty import fg, bg, ef, rs, Style, RgbBg
from terminal import Terminal

TERMINAL = "TERMINAL"
WINDOW = "WINDOW"
options = ["exit", "terminal", "window"]


def terminal_mode(terminal: Terminal):
    """
    starts a game with the terminal settings
    @param terminal: the terminal game object
    """
    game = terminal
    # cleanup mode selection
    Terminal.clear()

    # get the name of the user and cleanup (1 line max)
    name = game.get_name()
    game.del_n_lines(1)

    # get the dimensions and cleanup
    dim = game.get_dim(name)
    game.del_n_lines(1)
    
    # set size and name properties
    game.finish_init(name, dim)

    # update mode
    update = False

    # main game loop
    while not game.won():
        # update player info
        game.player_info()

        # print the board
        print(repr(game.board))

        # store the old color option
        old_option = game.option

        # print the color options - selected color should be updated
        game.color_selector()

        # update the board with selection made
        game.board.update(game.option)
        # cleanup and reprint the board

    if(game.won()):
        # update player info one last time
        game.player_info()

        # print the board one last time
        print(repr(game.board))

        print("You won! You have completed a {d}x{d} board in {moves} moves!".format(d = dim, moves = game.player.score))


def window_mode():
    """
    sets up the window version of the game

    attributes
    ----------
    # TODO
    """
    print("you have entered window mode")

def main():
    terminal = Terminal()
    mode = terminal.mode_selector()

    if mode == TERMINAL:
        terminal_mode(terminal)
    else:
        window_mode()

if __name__ == "__main__":
    main()