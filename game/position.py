
class Position:
    """
    position object in a 2D board

    attributes
    ----------
    x: int
        x coord
    y: int
        y coord
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    @property
    def x(self) -> int:
        """
        getter for x coord
        """
        return self._x

    @x.setter
    def x(self, x: int):
        """
        setter for x attribute

        params
        ------
        x: int
            int val to set coord to
        """
        self._x = x
    
    @property
    def y(self) -> int:
        """
        setter for y coord
        """
        return self._y
    
    @y.setter
    def y(self, y:int):
        """
        setter for y attribute

        params
        ------
        y: int
            int val to set coord to
        """
        self._y = y

    def __str__(self) -> str:
        """
        creates string representation of position
        tuple form
        """
        return "(" + str(self.x) + ", " + str(self.y) + ")"