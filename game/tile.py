from position import Position

class Tile:

    def __init__(self, pos: Position, color: str, active = False):
        self.active = active
        self._pos = pos
        self.color = color

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
        return str(self.color)
# tile = Tile(Position(1,1), "red")
# print(tile)


    