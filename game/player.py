
class Player:


    """
    class representing a player with simple attributes

    attributes
    ----------
    name: str
        name of the player
    score: int
        score of player during the game
        - starts at 0
    """
    def __init__(self, name: str):
        self.name = name
        self._score = 0
    
    @property
    def name(self) -> str:
        """
        getter for name attribute
        """
        return self._name
    
    @name.setter
    def name(self, name: str):
        """
        setter for name attribute

        params
        ------
        name: str
            name to give player
        """
        self._name = name

    @property
    def score(self) -> int:
        """
        getter for score attribute
        """
        return self._score
    
    @score.setter
    def score(self, delta: int):
        """
        setter for score attribute

        params
        ------
        delta: int
            change in score to apply
        """
        self._score += delta

    def __str__(self) -> str:
        """
        returns string version of this player
        """
        return "Player: " + str(self.name) + "\tMoves: " + str(self.score)
