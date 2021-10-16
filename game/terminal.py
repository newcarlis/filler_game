import os
import sys
import color
from color import Color
from player import Player
from board import Board
from tile import Tile
from position import Position
import time
from sty import fg, bg, ef, rs, Style, RgbBg
import keyboard
from game import Game
from errors import *

options = ["exit", "terminal", "window"]
TERMINAL = "TERMINAL"
WINDOW = "WINDOW"

class Terminal(Game):
    def __init__(self, size: int = 0, player: Player = " "):
        self.option = ""
        # self.size = 0
        # self.Player = None

    def finish_init(self, name: str, dim: int):
        self.size = dim
        super().__init__(self.size, Player(name))
        self._option = self.board.get_tile(Position(0, 0)).color

    @property
    def option(self) -> Color:
        return self._option

    @option.setter
    def option(self, color: Color):
        self._option = color

    def player_info(self):
        Terminal.up_n_lines((self.size * 2) + 3)
        print(str(self.player) + "    ")

    @staticmethod
    def clear():
        """
        clears the entire terminal and
        and goes back to the top
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def del_n_lines(n: int):
        for i in range(n):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")

    @staticmethod
    def up_n_lines(n: int):
        for i in range(n):
            sys.stdout.write("\033[F")

    @staticmethod
    def loading(message: str):
        Terminal.clear()
        const = ". . . "
        message = message + const
        print(message)

        for i in range(3):
            # sleep
            time.sleep(1)
            # remove a dot form message
            message = message[:-2]
            # go up and to the start and reprint message
            Terminal.clear()
            print(message)
        time.sleep(1)
        # at the end rewrite main prompt

        Terminal.clear()

    @staticmethod
    def color_op(option):
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
            
            if tipo == "down":
                # movement to the left
                if key == "left":
                    if option <= 0:
                        # no change
                        show = False
                    else:
                        option -= 1
                        show = True
                        sel = True

                elif key == "right":
                    if option >= maxi:
                        # no change
                        show = False
                    else:
                        option += 1
                        show = True   
                        sel = True

                elif key == "esc":
                    exit()
                
                elif key == "enter":
                    # update selected color
                    new_color = color.get_color_at_index(option)

                    if self.option != new_color:
                        self.option = new_color
                        self.player.score = 1
                    return 

                else:
                    continue

                if show:
                    # reprint color options
                    Terminal.up_n_lines(1)
                    self.color_op(option)

    @staticmethod
    def get_name():
        # TODO error check the name so that is no longer than 8 ch
        # TODO fi xissue with hitting enter
        name_mssg = "enter your user name: "

        while True:
            try:
                name = input(name_mssg)

                if len(name) < 2 or len(name) > 16:
                    raise NameLengthError(name)

                return name

            except NameLengthError as error:
                Terminal.loading(error.message)
                continue

    def get_dim(self, name):
        """
        interacts with user to get dimensions
        sets the dimensions for board
        """

        dim_mssg = "{n}, enter board dimensions (4 - 15): ".format(n=name)
        
        while True:
            answer = input(dim_mssg)
            dim = 0
            try:
                dim = int(answer)

                if dim > 15 or dim < 4:
                    raise DimensionError(dim)

                return dim
            except DimensionError as error:
                Terminal.loading(error.message)
                continue

    @staticmethod
    def esc_mssg():
        print("press 'esc' to exit game any time.")

    @staticmethod
    def print_modes(selector):
        """
        prints the different game modes with an arrow on the current
        @param selector: indicated which option user is looking at
        """
        modes = ""
        uni = "\u27A4"
        sep = "\n"
        
        for i in range(len(options)):
            if i == len(options) - 1:
                sep = ""
            if i == selector:
                modes += uni
                modes += "  "
            
            else:
                modes += "   "
            modes += (options[i] + sep)
        print(modes)

    @staticmethod
    def mode_selector() -> str:
        """
        allows the user to select the game mode
        """
        selection = 0
        show = True
        
        # clear screen before mode selection
        Terminal.clear()
        print("Welcome to the Tile Game!")
        Terminal.print_modes(selection)
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
                    return TERMINAL
                elif selection == 2:
                    return WINDOW
                show = False
                return
            elif tipo == "down" and key == "esc":
                exit()
            
            if show:
                Terminal.up_n_lines(3)
                Terminal.print_modes(selection)
