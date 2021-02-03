import turtle
from matrix_struct import *
"""
file that takes care of displaying game board 
"""


def init(matrix: Matrix):
    # each square is going to be 30 pixels
    width = matrix.size * 100
    height = width + 200



    turtle.setup(width, height)
    turtle.setpos(0, 0)

    for row in range(matrix.size):
        for col in range(matrix.size):
            draw_square(matrix.board[row][col])


def draw_square(sqr: Square):
    turtle.up()
    turtle.goto(sqr.row * 30, sqr.col * 30)
    turtle.setheading(0)

    turtle.color(sqr.content)
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(30)
        turtle.right(90)
    turtle.end_fill()





def main():
    matrix = init_matrix(4)
    turtle.speed(0)
    # print(matrix)
    init(matrix)


main()