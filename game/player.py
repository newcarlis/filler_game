
class Player:
    
    def __init__(self, name: str):
        self.name = name
        self._score = 0
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, delta: int):
        self._score += delta

    def __str__(self):
        return "Player: " + str(self.name) + "\tscore: " + str(self.score)
