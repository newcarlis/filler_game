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
        self.window.resizable(False, False)

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
        play = Button(menu, width = 2, height = 1, bg = colors[0], borderwidth=0, command = self.open_intro)
        play.place(x = idx, y = idy)

        # play.bind('<Enter>', play.config(background='black'))

        idy += y_incre
        HTP = Button(menu, width = 2, height = 1, bg = colors[1], borderwidth=0, command= self.HTP).place(x = idx, y = idy)
        idy += y_incre
        exit = Button(menu, width = 2, height = 1, bg = colors[2], borderwidth=0, command=self.window.destroy).place(x = idx, y = idy)

        # resets the y index value to place first button | sets x index
        idy = init_y
        idx = x_labels

        play_label = Label(menu, text="    Play   ", font = ("canyon", 15)).place(x = idx, y = idy)
        idy += y_incre
        HTP_label= Label(menu, text="How to Play", font = ("canyon", 15)).place(x = idx, y = idy)
        idy += y_incre
        exit_label = Label(menu, text="    Exit   ", font = ("canyon", 15)).place(x = idx, y = idy)

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

    def clear(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def back_to_start(self):
        self.clear()
        self.start()

    def open_intro(self):
        self.clear()
        self.window.geometry("500x300")

        profile = Label(self.window, text="Game Info", font = ("atmosphere", 32))
        profile.pack(side=TOP)

        num_of_tiles = self.dim // self.dec_dim
        x = 0
        y = 50
        for i in range(num_of_tiles):
            temp = Frame(self.window, width = self.dec_dim, height = self.dec_dim, bg = get_hex_color(1), pady = 10).place(x = x, y = y)
            x += self.dec_dim

        name = Label(self.window, text="Username", font = ("cayon", 15)).place(x = 125, y = 120)
        name_box = Entry(self.window).place(x = 230, y = 125)

        grid_size = Label(self.window, text = 'Grid Size', font=("cayon", 15)).place(x = 125, y = 170)
        grid_box = Entry(self.window).place(x = 230, y = 175)

        enter = Button(self.window, width = 6, height = 1, text = "Next", font = ("cayon", 12), bg = "#b4cc6e", fg = "white", borderwidth=0).place(x=400, y=240)
        back = Button(self.window, width = 6, height = 1, text = "Back", font = ("cayon", 12), bg = "#a13c37", fg = "white", borderwidth=0, command=self.back_to_start).place(x=40, y=240)

        x = 0
        y = 300 - self.dec_dim
        for i in range(num_of_tiles):
            temp = Frame(self.window, width = self.dec_dim, height = self.dec_dim, bg = get_hex_color(1), pady = 10).place(x = x, y = y)
            x += self.dec_dim

    def HTP(self):

        self.clear()
        self.window.geometry("500x500")

        txt = Label(self.window, text="How to Play", font = ("atmosphere", 32))
        txt.pack(side=TOP)

        num_of_tiles = self.dim // self.dec_dim
        x = 0
        y = 50
        for i in range(num_of_tiles):
            temp = Frame(self.window, width = self.dec_dim, height = self.dec_dim, bg = get_hex_color(1), pady = 10).place(x = x, y = y)
            x += self.dec_dim

        back = Button(self.window, width = 6, height = 1, text = "Back", font = ("cayon", 12), bg = "#a13c37", fg = "white", borderwidth=0, command=self.back_to_start).place(x=40, y=440)

        x = 0
        y = 500 - self.dec_dim
        for i in range(num_of_tiles):
            temp = Frame(self.window, width = self.dec_dim, height = self.dec_dim, bg = get_hex_color(1), pady = 10).place(x = x, y = y)
            x += self.dec_dim

