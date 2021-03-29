import sys

class Game:
    
    def __init__(size: int, player: str):
        self.board = Board(size)
        self._player = Player(player)

    def won(self) -> bool:
        color = self.board[0][0]

        for tile in self.board.__iter__():
            if tile.color != color:
                return False
        
        return True

def terminal_mode():
    return

def window_setup():
    return

def main(invalid_counter = 1):
    mode = input("what mode would you like?\n[1]: terminal\n[2]: window\n")

    if mode == "1":
        terminal_mode()
    if mode == "2":
        window_mode()
    if invalid_counter == 3:
        print("Too many invalid attempts. Closing the program.")
    else:
        print("'%s' is not valid input. Try again\n" %mode)
        invalid_counter += 1
        main(invalid_counter)

if __name__ == "__main__":
    main()