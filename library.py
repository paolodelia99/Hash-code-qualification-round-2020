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
