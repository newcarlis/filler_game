import data
import turtle
from filler import accept_move
"""
file that takes care of all displays displaying game board 
"""


def init_win(game: data.Game):
    """
    initializes the game window to the necessary measurements
    :param game: the game
    :return: game
    """
    # matrix in use during the game
    matrix = game.matrix
    # makes the turtle draw everything before displaying
    turtle.tracer(200, 200)

    # size the window so all elements can fit
    width = (matrix.size * data.SQR_SIZE) + data.PADDING + data.COLOR_SPACE
    height = (matrix.size * data.SQR_SIZE) + data.PADDING + data.INFO_SPACE

    # background color | Dark gray
    turtle.bgcolor(data.BG_COLOR)

    # sets up the world and appropriately sizes the window
    turtle.Screen().setup(width, height)
    turtle.Screen().setworldcoordinates(data.H_OFFSET, data.V_OFFSET, width + data.H_OFFSET, height + data.V_OFFSET)

    # hide turtle before drawing
    turtle.hideturtle()

    # draws the entire matrix
    draw_board(matrix)

    # draw the player info section
    turtle.up()

    # user info
    set_user(game)

    # draw the moves display
    set_moves(game)

    turtle.up()
    turtle.home()
    game = color_menu(game)

    return game


def set_user(game: data.Game):
    # go above matrix
    turtle.goto(0, (game.matrix.size * data.SQR_SIZE) + data.INFO_PADD)
    turtle.color("black")
    turtle.write(game.player.name, font=("Courier", 12, 'normal'))


def draw_board(matrix: data.Matrix):
    # loops trough the matrix board and draws each square
    for row in range(matrix.size):
        for col in range(matrix.size):
            draw_square(matrix.board[row][col], matrix.size)


def draw_square(sqr: data.Square, size: int):
    """
    used the information associated with the square to draw it on the board
    :param sqr: the square to be drawn
    :param size: size of the board. needed for measurements
    :return: TODO: return type
    """

    turtle.up()
    # convert the coords (0-7..15..24) to scale
    # EX: sqr with coords(0,0) has the position (0, height of matrix)
    x = (sqr.col * data.SQR_SIZE)
    y = (size * data.SQR_SIZE) - (sqr.row * data.SQR_SIZE)
    turtle.goto(x, y)
    # code to draw a square
    # make sure the turtle is pointing down
    turtle.setheading(270)

    # set the color
    turtle.color(sqr.color)
    turtle.down()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(data.SQR_SIZE)
        turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.update()


def set_moves(game: data.Game):
    """
    updates the number of moves as the player plays.
    :param game: the current game being used
    :return: NONE
    """

    # the matrix
    matrix = game.matrix
    # go to the position where moves are displayed
    x = (matrix.size * data.SQR_SIZE) + data.INFO_PADD_2
    y = (matrix.size * data.SQR_SIZE) + data.INFO_PADD
    turtle.goto(x, y)
    turtle.color(data.BG_COLOR)

    if game.player.moves > 0:
        turtle.setheading(0)
        turtle.forward(72)
        turtle.begin_fill()
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(15)
        turtle.left(90)
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(15)
        turtle.left(90)
        turtle.end_fill()

        # get the moves and update
        turtle.color('black')
        moves = str(game.player.moves)
        turtle.write(moves, font=("Courier", 12, 'normal'))

    else:
        # get the moves and update
        turtle.color('black')
        moves = "Moves: " + str(game.player.moves)
        turtle.write(moves, font=("Courier", 12, 'normal'))


def color_menu(game: data.Game):
    """
    Creates the color menu to the right of the board.
    equally spaces the colors so it looks neat
    :param game: the current game used
    :return: the list of color items
    """
    matrix = game.matrix
    # this determines where to place the color blocks so they are evenly spaced
    color_spacing = ((matrix.size * data.SQR_SIZE) - (len(data.COLORS) * data.SQR_SIZE)) / (len(data.COLORS) - 1)
    padding = (data.COLOR_SPACE - data.SQR_SIZE) / 2
    turtle.goto((matrix.size * data.SQR_SIZE + padding), matrix.size * data.SQR_SIZE)

    # point down before drawing each
    turtle.setheading(270)

    # the list containing the locations of all colors
    color_map = []

    for color in data.COLORS:
        turtle.color('black', color)

        # create the color item and store it
        the_color = data.ColorItem(turtle.xcor(), turtle.ycor(), color)
        color_map.append(the_color)

        turtle.down()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(data.SQR_SIZE)
            turtle.left(90)
        turtle.end_fill()

        turtle.up()
        turtle.forward(color_spacing + data.SQR_SIZE)

    game.color_map = color_map
    return game


def toggle_screen_click(option: bool, game):

    if option:
        turtle.listen()
        turtle.onscreenclick(lambda x, y:
                             accept_move((x, y), game))

    else:
        turtle.onscreenclick(None)
