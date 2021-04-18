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
MODE = "MODE"
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
    def __init__(self, mode = MODE, selection = 0):
        self._mode = mode
        self.aceept_in = True
        self._selection = selection
        
    def finish_init(self):
        name = input("enter your name: ")
        # size = int(input('board dimension: '))
        # size = 4
        # player = Player(name)
        # Game.__init__(self, size, player)

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode: str):
        self._mode = mode

    @property
    def selection(self):
        """ selection getter """
        return self._selection

    @selection.setter
    def selection(self, delta):
        # print("delta " + str(delta))
        if (self._selection + delta) == -1 or (self.selection + delta) == 3:
            # print("selection " + str(self.selection) + " cannot be updated")
            return False
        else:
            self._selection+= delta
            # print(self.selection)
            return True

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
            on_release= (lambda key:
                self.on_release(key)
            )) as listener:
            listener.join()
        return False

    def on_press(self, key):
        k = format(key)

        if self.mode == MODE:
            prev = self.selection
            if k == "Key.down":
                # print("pressed down")
                self.selection = 1

            elif k == "Key.up":
                # print("pressed up")
                self.selection = -1

            elif k == "Key.enter":
                if self.selection == 0:
                    exit()
                elif self.selection == 1:
            #         self.del_n_lines(len(options) + 1)
            #         self.finish_init()
                    self.mode = INIT_MODE
                    
            
            # if there is a change, update the view
            if prev != self.selection:
                    self.del_n_lines(len(options) + 1)
                    propmt_mode(self.selection)
        

    def on_release(slef, key):
        

        if key == keyboard.Key.enter:
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
    mode = ""
    sep = "\n"
    for i in range(len(options)):
        if i == len(options) - 1:
            sep = ""
        if i == selector:
            mode += "\u27A4  "
        
        else:
            mode += "   "
        mode += (options[i] + sep)
    print(mode)

def main():
    # name = input("enter your name: ")

    tempT = Terminal()
    propmt_mode()
    tempT.init_key_input()
    tempT.finish_init()

    # print("dghdshgdbgsnasnnrsnryn\ngsgsfgrhfbht\ngwrgragrg")

    # print("\033[1;1f")
    # print("\033[" + str(4) + "A")
    # print(" \033[K")
    

if __name__ == "__main__":
    main()