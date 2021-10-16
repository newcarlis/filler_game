from game import Game

class Window(Game):

    def __init__(self, size: int, player: Player, window=None):
        super().__init__(size, player)
        self.name = "carly"
        self.window = window
        self.PLAYBAR = 50 # vertical dimension
        self.SIDEPAD = 50 # horizontal dimension

    def finish_init(self, window, name = "carly", dim = 4):
        super().__init__(dim, Player(name))
        self.window = window

    def update_play_bar(self):
        font = pygame.font.Font("candara", 12)
        text = font.render(self.name, True, "white")
        print("here goes the player bar")

