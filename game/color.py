from enum import Enum
import random

class Color(Enum):
    RED = (161,60,55)
    GREEN = (180,204,110)
    YELLOW = (222,167,58)
    PURPLE = (107,53,184)
    BLUE = (50,146,173)
    


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