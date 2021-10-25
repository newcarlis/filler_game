from tkinter import * 
from color import get_hex_color
import pyglet

class Window():

    def __init__(self):
        self.name = "carly"
        self.dim = 500
        self.dec_dim = int(self.dim * 0.04)
        self.window = Tk()
        self.game = object

    @staticmethod
    def import_fonts():
        pyglet.font.add_file('fonts/Atmosphere-Regular.TTF')
        atmosphere = action_man = pyglet.font.load('Atmosphere Regular')

        pyglet.font.add_file('fonts/Canyon_Regular.OTF')
        canyon = action_man = pyglet.font.load('Canyon Regular')

    def get_top_dec(self) -> int:
        # % of horizontal dimension
        width = int(self.dim * .25)
        # amount of tiles that can fit on allocated width
        count = int(width // self.dec_dim)

        # vertical height of stacked tiles
        height = count * self.dec_dim

        for i in range(count, 0, -1):
            for j in range(i):
                temp_tile = Frame(self.window, bg = get_hex_color(1)[0], width = self.dec_dim, height = self.dec_dim).place(x = j * self.dec_dim, y = (count - i) * self.dec_dim)

        return count

    def get_bottom_dec(self):
        # % of horizontal dimension
        width = int(self.dim * .60)
        # amount of tiles that can fit on allocated width
        count = int(width // self.dec_dim)

        # vertical height of stacked tiles
        height = count * self.dec_dim
        for row in range(1, count + 1):
            for col in range(1, row + 1):
                x = self.dim - ((col) * self.dec_dim)
                y = self.dim - ((count - row + 1) * self.dec_dim)
                # print(row, col, x, y, sep="\t")
                temp_tile = Frame(self.window, bg = get_hex_color(1)[0], width = self.dec_dim, height = self.dec_dim).place(x = x, y = y)

    def get_menu(self, margin: int):

        index = self.dec_dim
        px = 20
        py = 20
        init_y = margin + self.dec_dim * 3
        idx = margin + self.dec_dim * 2
        idy = init_y

        x_labels = margin + self.dec_dim * 5
        # increments y index
        y_incre = self.dec_dim * 3

        menu = Frame(self.window, width = 200, height = 200, padx = px, pady = py).place(x = margin, y = margin + self.dec_dim)

        colors = get_hex_color(3)
        play_frame = Button(menu, text = "", width = 2, height = 1, bg = colors[0], borderwidth=0).place(x = idx, y = idy)
        idy += y_incre
        HTP_frame = Button(menu, width = 2, height = 1, bg = colors[1], borderwidth=0).place(x = idx, y = idy)
        idy += y_incre
        exit_frame = Button(menu, width = 2, height = 1, bg = colors[2], borderwidth=0).place(x = idx, y = idy)

        # resets the y index value to place first button | sets x index
        idy = init_y
        idx = x_labels

        play = Label(menu, text="    Play   ", font = ("canyon", 15)).place(x = idx, y = idy)
        idy += y_incre
        HTP = Label(menu, text="How to Play", font = ("canyon", 15)).place(x = idx, y = idy)
        idy += y_incre
        exit = Label(menu, text="    Exit   ", font = ("canyon", 15)).place(x = idx, y = idy)

        # play_frame.pack()
        # HTP_frame.pack()
        # exit_frame.pack()

        # play.pack()
        # HTP.pack()
        # exit.pack()

        return menu

    def start(self):

        Window.import_fonts()

        self.window.geometry(f"{self.dim}x{self.dim}")
        self.window.title("Tile")

        left_margin = (self.get_top_dec() - 1) * self.dec_dim
        self.get_bottom_dec()

        intro_msg = "Tiles Game"
        intro_label = Label(self.window, text=intro_msg, font = ("atmosphere", 32), pady = self.dec_dim * 3)
       
        intro_label.pack(anchor=NE, padx = (0, left_margin))

        self.get_menu(left_margin)

        self.window.mainloop()





