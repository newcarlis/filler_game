import sys

class Game:
    """
    class that manages the game and the logic
    as it is played.

    also prompts the user for the game mode

    attributes
    ----------
    player: Player
        object of the player using game
    size: int
        size of the game board
    """
    def __init__(size: int, player: str):
        self.board = Board(size)
        self._player = Player(player)

    def won(self) -> bool:
        """
        determines if games has finished and player won
        """
        color = self.board[0][0]

        for tile in self.board.__iter__():
            if tile.color != color:
                return False
        
        return True

def terminal_mode():
    """
    sets up the terminal game mode

    attributes
    ----------
    # TODO
    """
    return

def window_mode():
    """
    sets up the window version of the game

    attributes
    ----------
    # TODO
    """
    return

def main(invalid_counter = 1):
    mode = input("what mode would you like?\n[1]: terminal\n[2]: window\n[x]: cancel\n").strip()

    if mode == "1":
        terminal_mode()
    elif mode == "2":
        window_mode()
    elif mode == "x":
        return
    elif invalid_counter == 3:
        print("Too many invalid attempts. Closing the program.")
    else:
        print("'%s' is not valid input. Try again\n" %mode)
        invalid_counter += 1
        main(invalid_counter)

if __name__ == "__main__":
    main()