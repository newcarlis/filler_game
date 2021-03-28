from position import Position

class Tile:

    def __init__(self, position, color: str, active = False):
        self.active = active
        self._position = position
        self.color = color

    @property
    def active(self):
        return 

    @active.setter
    def active(self, bool):
        self._active = bool

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, position: Position):
        self._position = position

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color: str):
        self._color = color


   
tile = Tile(Position(1,1), "red")
print(tile.__dict__)
# print(tile.__dict__)


    