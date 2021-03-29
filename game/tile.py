from position import Position
import color
from sty import fg, bg, ef, rs, Style, RgbBg

class Tile:
    # TODO: modify tile position to be within board - not given
    def __init__(self, pos: Position):
        self.active = False
        self.pos = pos
        self.color = color.get_color()

    @property
    def active(self):
        return 

    @active.setter
    def active(self, bool):
        self._active = bool

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos: Position):
        self._pos = pos

    @property
    def color(self) -> str:
        return self._color
    
    @color.setter
    def color(self, color: str):
        self._color = color

    def __str__(self) -> str:
        return "Tile { \n pos: %s \n color: %s \n active: %s \n}"%(self.pos, self.color, self.active)
   
    def __repr__(self):
        return str(bg(self.color[0], self.color[1], self.color[2]) + "  " + bg.rs)



    