class Book:
    """
    A class representing the book
    """

    def __init__(self, id, score):
        self.id = id
        self.score = score

    def __eq__(self, other):
        if other is None:
            return False

        if other is self:
            return True

        if other.id == self.id and other == self.score:
            return True
        else:
            return False
