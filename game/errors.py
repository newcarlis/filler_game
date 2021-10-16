
class NameLengthError(Exception):
    # raised when the name provided by user is not within range

    def __init__(self, name: str) -> None:
        self.name = name
        self.message = ""

        if len(name) < 2:
            self.message = "Name is too short. Try again"
        
        elif len(name) > 16:
            self.message = "Name is too long. Try again"

class DimensionError(Exception):
    # raised when the dimension provided is not within range

    def __init__(self, dim: int) -> None:
        self.dim = dim
        self.message = ""

        if dim > 15:
            self.message = str(dim) + " is too big. Try a smaller number"

        elif dim < 4:
            self.message = str(dim) + " is too small. Try a larger number"
                        
        else:
            self.message = str(answer) + " is not valid. Try again"
