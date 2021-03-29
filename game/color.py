from enum import Enum
import random

class Color(Enum):
    RED = (255,46,23)
    BLUE = (56,9,232)


def get_color() -> str:
    num = random.randint(0, len(Color) - 1)
    counter = 0
    color = ""
    # print(num)
    for tone in Color:
        # print(tone.value)
        if counter == num:
            color = tone.value
            break
        else:
            counter += 1
    
    return color