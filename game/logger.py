"""
this file edits a file where the changes made in the game are reported 
and logged for debugging puposes
"""

import color

FILE = ""
COLOR = "{user} selected: {color}"
USER = "{user} playing"
OUT = "{user} decided to exit"
DIM = "creating board with {num} tiles"
NAME = ""

def create_log(name: str = 'log.txt'):
    """
    initializes the log file

    """
    global FILE 
    FILE = name
    open(name, "w")



def log(msg: str):

    try:
        file = open(FILE, "a")
        file.write(msg + "\n")
        file.close()
        return True

    except(FileNotFoundError):
        return False

def log_color(c: color.Color):
    log(COLOR.format(user = NAME, color = c.name))

def log_dim(dim: int):
    log(DIM.format(num = dim))

def log_user(name: str):
    global NAME
    NAME = name
    log(USER.format(user = NAME))

def log_exit():
    log(OUT.format(user = NAME))

