from tkinter import * 
from color import get_hex_color
import pyglet

class Window():

    def __init__(self):
        self.name = "carly"
        self.dim = 500
        self.dec_dim = self.dim * 0.04
        self.window = Tk()
        self.game = object

    @staticmethod
    def import_fonts():
        pyglet.font.add_file('fonts/Atmosphere-Regular.TTF')
        atmosphere = action_man = pyglet.font.load('Atmosphere Regular')

    def get_top_dec(self):
        # % of horizontal dimension
        width = int(self.dim * .25)
        # amount of tiles that can fit on allocated width
        count = int(width // self.dec_dim)

        # vertical height of stacked tiles
        height = count * self.dec_dim

        for i in range(count, 0, -1):
            for j in range(i):
                # temp_tile = Frame(main_frame, bg = get_hex_color(), width = self.dec_dim, height = self.dec_dim).grid(row = j, column = (count - i))
                temp_tile = Frame(self.window, bg = get_hex_color(), width = self.dec_dim, height = self.dec_dim).place(x = j * self.dec_dim, y = (count - i) * self.dec_dim)

    def get_bottom_dec(self):
        # % of horizontal dimension
        width = int(self.dim * .65)
        # amount of tiles that can fit on allocated width
        count = int(width // self.dec_dim)

        # vertical height of stacked tiles
        height = count * self.dec_dim
        for row in range(1, count + 1):
            for col in range(1, row + 1):
                x = self.dim - ((col) * self.dec_dim)
                y = self.dim - ((count - row + 1) * self.dec_dim)
                # print(row, col, x, y, sep="\t")
                temp_tile = Frame(self.window, bg = get_hex_color(), width = self.dec_dim, height = self.dec_dim).place(x = x, y = y)

    def start(self):

        Window.import_fonts()

        self.window.geometry(f"{self.dim}x{self.dim}")
        self.window.title("Tile")

        self.get_top_dec()
        self.get_bottom_dec()

        # menu = Frame(self.window)

        intro_msg = "Tiles Game"
        intro_label = Label(self.window, text=intro_msg, font = ("atmosphere", 30), pady = self.dec_dim * 2)
        # play = Button(menu, text="Play")
        # HTP = Button(menu, text="How to Play")
        # exit = Button(menu, text="Exit")

        intro_label.pack()
        # intro.pack()

        # top_frame.pack(side = TOP, anchor = NW, fill=X, expand=True)

        # play.pack()
        # HTP.pack()
        # exit.pack()
        # menu.pack(fill=BOTH)

        self.window.mainloop()





