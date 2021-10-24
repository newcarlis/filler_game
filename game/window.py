from tkinter import * 
from color import get_hex_color

class Window():

    def __init__(self):
        self.name = "carly"
        self.dim = 500
        self.dec_dim = 20
        self.window = Tk()
        self.game = object

    def start(self):
        self.window.geometry("500x500")
        self.window.title("Tile")

        left_dim = int((0.25 * self.dim)//self.dec_dim)
        frame_dim = self.dec_dim * left_dim
        left_dec = Frame(self.window, height=frame_dim, width=frame_dim, bg="black")

        intro = Frame(self.window)
        menu = Frame(self.window)

        print(frame_dim)

        for line in range(left_dim, 0, -1):
            line_frame = Frame(left_dec, bg="pink", height=self.dec_dim - 5, width=frame_dim)
        #     for tile in range(line):
        #         frame = Frame(left_dec, bg = get_hex_color(), width = self.dec_dim, height = self.dec_dim)
        #         frame.pack(side=LEFT)

            line_frame.pack(side=TOP)
        left_dec.pack(side=TOP, anchor=NW)

        intro_msg = "Tiles Game"
        intro_label = Label(intro, text=intro_msg)
        play = Button(menu, text="Play")
        HTP = Button(menu, text="How to Play")
        exit = Button(menu, text="Exit")

        intro_label.pack()
        intro.pack()
        play.pack()
        HTP.pack()
        exit.pack()
        menu.pack()
        
        # frame = Frame(self.window, bg="red", width=20, height=20)
        # frame.pack(side=LEFT)

        self.window.mainloop()




