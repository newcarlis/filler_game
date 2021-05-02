import sys
from color import Color
import color
from player import Player
from board import Board
from tile import Tile
from position import Position
import curses
import time
import re
from sty import fg, bg, ef, rs, Style, RgbBg
import keyboard

COLR_MODE = "COLR"
INIT_MODE = "INIT"
NAME_MODE = "NAME"
WINDOW = "WINDOW"
MODE = "MODE"
DIM_MODE = "DIM"
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

    @property
    def player(self) -> Player:
        return self._player
    
    @player.setter
    def player(self, player: Player):
        self._player = player
    # TODO add player property

    def won(self) -> bool:
        """
        determines if games has finished and player won
        """
        color = self.board.get_tile(Position(0,0)).color

        for tile in self.board.__iter__():
            if tile.color != color:
                return False
        print("won")
        return True

class Terminal(Game):
    def __init__(self):
        self.mode = ""
        self.option = ""
        
    def finish_init(self, name: str, dim: int):
        super().__init__(dim, Player(name))

    @property
    def option(self) -> Color:
        return self._option

    @option.setter
    def option(self, color: Color):
        self._option = color

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode: str):
        self._mode = mode

    def clear(self):
        """
        clears the entire terminal and
        and goes back to the top
        """
        print("\033[2J")

    def move_up_n_lines(self, n: int):
        """
            moves the cursor up by n lines and back left
        """
        print("\033[" + str(n) + "F")

    def move_right_n_lines(self, n: int):
        """
        moves to the right by n columns
        """
        print("\033[" + str(n) + "C")
    
    def goto(self, x: int, y: int):
        print("\033[" + str(x) + ';' + str(y) + "f")

    def player_info(self, update: bool = False):
        """
        updates the player info during the game
        TODO: add params
        """
        if update:
            # move up by 1(color line) + 1(gap) + len(board) + 1(this line) in the end
            # + 1(compensate for print) then... update score
            self.move_up_n_lines(self.board.vertical_span + 4)
        print(self.player)

    def del_n_lines(self, n: int = 0):
        """
        deletes n number of lines from the terminal
        :param: n, number of lines
        """
        string = ""
        # go up and back and delete n times
        for i in range(n):
            string = string + "\033[1A" + "\r" + "\033[K"
        print(string)
        # go back one more time to undo the '\n's
        print("\033[2A")

    def color_op(self, option):
        colores = ""
        counter = 0
        for tone in Color:
            color = tone.value
            if counter == option:
                colores += (bg(color[0], color[1], color[2]) + " \u2573 " + bg.rs + "\t")
                counter += 1
            else:
                colores += (bg(color[0], color[1], color[2]) + "   " + bg.rs + "\t")
                counter += 1
        
        print(colores)

    def color_selector(self):
        """
        allows user to move the cursor to select a color
        """
        option = 0
        show = True
        self.color_op(option)
        maxi = len(Color) - 1 # amount of colors
        sel = False
        while True:
            # read event and parse it
            event = keyboard.read_event(suppress = True)
            tipo = event.event_type
            key = event.name

            # movement to the left
            if tipo == "down" and key == "left":
                if option <= 0:
                    # no change
                    show = False
                else:
                    option -= 1
                    show = True
                    sel = True

            elif tipo == "down" and key == "right":
                if option >= maxi:
                    # no change
                    show = False
                else:
                    option += 1
                    show = True   
                    sel = True

            elif key == "esc":
                exit()
            
            elif key == "enter" and sel:
                # update selected color
                self.option = color.get_color_at_index(option)
                self.player.score = 1
                return 

            # TODO: all other cases and print invalid output
            if show:
                # cleanup
                self.del_n_lines(1)
                # reprint
                self.color_op(option)

    def get_name(self):
        # TODO error check the name so that is no longer than 8 ch
        name_mssg = "enter your user name: "
        name = input(name_mssg)
        return name
    
    def get_dim(self):
        """
        interacts with user to get dimensions
        sets the dimensions for board
        """

        dim_mssg = "enter board dimensions (max 15): "
        while True:
            answer = input(dim_mssg)
            dim = -1
            try:
                dim = int(answer)

                if dim > 15:
                    raise ValueError

                return dim
            except ValueError:
                if dim > 15:
                    error = str(dim) + " is too big. Try a smaller number. . . . . "
                else:
                    error = str(answer) + " is not valid. Try again. . . . . "

                print(error)

                for i in range(5):
                    # sleep
                    time.sleep(1)
                    # remove a dot form error message
                    error = error[:-2]
                    # go up and to the start and reprint new error message
                    self.del_n_lines(1)
                    print(error)
                time.sleep(1)
                # at the end rewrite main prompt

                self.del_n_lines(2)
                continue

    def esc_mssg(self):
        print("press 'esc' to exit game any time.")

    def print_modes(self, selector):
        """
        prints the different game modes with an arrow on the current
        @param selector: indicated which option user is looking at
        """
        modes = ""
        sep = "\n"
        
        for i in range(len(options)):
            if i == len(options) - 1:
                sep = ""
            if i == selector:
                modes += "\u27A4  "
            
            else:
                modes += "   "
            modes += (options[i] + sep)
        print(modes)

    def mode_selector(self):
        """
        allows the user to select the game mode
        TODO: future update only updates the grid with the color
        """
        selection = 0
        show = True
        self.print_modes(selection)
        while True:
            # read user event
            event = keyboard.read_event(suppress = True)
            key = event.name
            tipo = event.event_type
            # print(key, tipo)
            if tipo == "down" and key == "down":
                if selection >= 2:
                    # print(selection)
                    show = False
                else:
                    selection += 1
                    show = True

            elif tipo == "down" and key == "up":
                if selection <= 0:
                    # print(selection)
                    show = False
                else:
                    selection -= 1
                    show = True

            elif tipo == "down" and key == "enter":
                if selection == 0:
                    # exit the game
                    exit()
                elif selection == 1:
                    # enable name mode
                    self.mode = NAME_MODE
                elif selection == 2:
                    self.mode = WINDOW
                show = False
                return
            elif tipo == "down" and key == "esc":
                exit()
            
            if show:
                self.del_n_lines(len(options))
                self.print_modes(selection)

def terminal_mode(terminal):
    """
    starts a game with the terminal settings
    @param terminal: the terminal game object
    """
    game = terminal
    
    # cleanup mode selection
    game.del_n_lines(len(options))

    # get the name of the user and cleanup (1 line max)
    name = game.get_name()
    game.del_n_lines(1)

    # get the dimensions and cleanup
    dim = game.get_dim()
    game.del_n_lines(1)

    # set size and name properties
    game.finish_init(name, dim)

    # update mode
    update = False

    # main game loop
    while not game.won():
        # update player info
        game.player_info(update)

        # print the board
        print(repr(game.board))

        # print the color options - selected color should be updated
        game.color_selector()

        # update the board
        game.board.update(game.option)
        # cleanup and reprint the board
        update = True


def window_mode():
    """
    sets up the window version of the game

    attributes
    ----------
    # TODO
    """
    return

def main():
    terminal = Terminal()
    terminal.mode_selector()
    terminal_mode(terminal)

if __name__ == "__main__":
    main()