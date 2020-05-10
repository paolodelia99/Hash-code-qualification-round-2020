class Library:
    """
    A class representing the library
    """

    def __init__(self, id, no_books, sign_up_time, book_per_day, books):
        self.id = id
        self.no_books = no_books
        self.sign_up_time = sign_up_time
        self.book_per_day = book_per_day
        self.books = books
        self.tot_score = sum([book.score for book in books])  # total score of the books of the library

    def get_books_ids(self):
        """

        @return: return a list containing the books ids
        """
        return [int(book.id) for book in self.books]

    def __eq__(self, other):
        if other is None:
            return False

        if other is self:
            return True

        if other.id == self.id and other.no_books and other.sign_up_time == self.sign_up_time and other.book_per_day == self.book_per_day and [
            a == b for a, b in zip(self.books, other.books)]:
            return True
        else:
            return False
