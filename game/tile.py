from position import Position
import color
from sty import fg, bg, ef, rs, Style, RgbBg

class Tile:
    """
    class that represents a tile on the game board

    attributes
    ----------
    position: Position
        position to place the tile at
    active: bool
        tells if the board is active - false by default
    color: Color
        color to give the Tile object
    """
    def __init__(self, pos: Position):
        self.active = False
        self.pos = pos
        self.color = color.get_color()

    @property
    def active(self) -> bool:
        """
        active bool setter - tells if tile is active
        """
        return self._active

    @active.setter
    def active(self, active: bool):
        """
        setter that activates/deactivates the tile

        params
        ------
        active: bool
            what the set the attribute to true/false
        """
        self._active = active

    @property
    def pos(self) -> Position:
        """
        getter for position of tile
        """
        return self._pos

    @pos.setter
    def pos(self, pos: Position):
        """
        setter for position of tile

        params
        ------
        pos: Position
            position to give tile
        """
        self._pos = pos

    @property
    def color(self) -> Color:
        """
        color getter
        """
        return self._color
    
    @color.setter
    def color(self, color: Color):
        """
        color setter for tile

        params
        ------
        color: Color
            color to assign this tile
        """
        self._color = color

    def __str__(self) -> str:
        """
        informal version of printing the tile
        shows all attributes for testing purposes
        """
        return "Tile { \n pos: %s \n color: %s \n active: %s \n}"%(self.pos, self.color, self.active)
   
    def __repr__(self) -> str:
        """
        formal version of printing tiles
        used in terminal version of game
        just displays color
        """
        return str(bg(self.color[0], self.color[1], self.color[2]) + "  " + bg.rs)



    