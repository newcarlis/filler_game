import sys
from color import Color
from player import Player
from board import Board
from tile import Tile
from position import Position
import curses
import time
from sty import fg, bg, ef, rs, Style, RgbBg
from pynput import keyboard

COLR_MODE = "COLR"
INIT_MODE = "INIT"

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
        self.board = Board(size)
        self._player = player

    def won(self) -> bool:
        """
        determines if games has finished and player won
        """
        color = self.board[0][0]

        for tile in self.board.__iter__():
            if tile.color != color:
                return False
        
        return True

class Terminal(Game):
    def __init__(self, mode = INIT_MODE):
        self.mode = mode
        self.aceept_in = True
        
    def finish_init(self):
        name = input("enter your name: ")
        size = int(input('board dimension: '))
        player = Player(name)
        Game.__init__(self, size, player)

    def clear(self):
        """
        clears the entire terminal and
        and goes back to the top
        """
        print("\033[2J")

    def del_n_lines(self, n: int = 0):
        """
        deletes n number of lines from the terminal
        :param: n, number of lines
        """
        print("\033[" + str(n) + "A")

    def color_op(self, option = 0):
        colores = ""
        counter = 0
        for tone in Color:
            color = tone.value
            if counter == option:
                colores += (bg(color[0], color[1], color[2]) + " \u2573 " + bg.rs + "\t")
                counter += 1
            else:
                colores += (bg(color[0], color[1], color[2]) + "    " + bg.rs + "\t")
                counter += 1
        
        return colores

    def init_key_input(self):
        with keyboard.Listener(
            on_press= (lambda key:
                self.on_press(key)),
            on_release=on_release
            ) as listener:
            listener.join()

    def on_press(self, key):
        k = format(key)
        
        if self.mode == INIT_MODE:
            print("taking initial input")
        

def on_release(key):
    
    if key == keyboard.Key.esc:
        # Stop listener
        return False

    
def terminal_mode():
    game = Terminal()
    # print(repr(game.board))
    # print(game.color_op())
    game.init_key_input()
    # self.init_key_input() # enable key input
    finish_init() # finish initializing this object



def window_mode():
    """
    sets up the window version of the game

    attributes
    ----------
    # TODO
    """
    return

def propmt_mode(selector = 0):
    options = ["exit", "terminal", "window"]
    mode = ""
    for i in range(len(options)):
        if i == selector:
            mode += "\u27A4  "
        else:
            mode += "   "
        mode += (options[i] + "\n")
    print(mode)

def main():
    
    prompt = propmt_mode()
    input(prompt)

if __name__ == "__main__":
    main()