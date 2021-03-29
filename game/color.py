from enum import Enum
import random

class Color(Enum):
    RED = "red"
    BLUE = "blue"

def get_color() -> str:
    num = random.randint(len(Color))
    counter = 0
    color = null
    for tone in Color:
        if counter == num:
            color = tone.value
        else:
            counter += 1
    
    return color