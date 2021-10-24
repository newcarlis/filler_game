from enum import Enum
import random

class Color(Enum):
    """
    Enum class of colors
    format: RGB
    """
    RED = (161,60,55)
    GREEN = (180,204,110)
    YELLOW = (222,167,58)
    PURPLE = (107,53,184)
    BLUE = (50,146,173)

def get_color() -> Color:
    """
    generates a random color from the enum
    """
    num = random.randint(0, len(Color) - 1)
    counter = 0
    color = ""
    for tone in Color:
        # print(tone)
        if counter == num:
            color = tone
            break
        else:
            counter += 1
    
    return color

def get_hex_color() -> Color:
    """
        translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % get_color().value

def get_color_at_index(index: int) -> Color:
    """
    returns the color at a given index
    """
    counter = 0
    for color in Color:
        if counter == index:
            return color

        else:
            counter += 1