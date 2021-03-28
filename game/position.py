
class Position:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x: int):
        self._x = x
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y:int):
        self._y = y