from solver import Library
from solver import Book


class ScenarioParser:

    def __init__(self, file_path):
        self.file_path = file_path

    @staticmethod
    def create_books_list(books_id, books_score):
        """Create the array of Books objects for the given library

        Arguments:
            books_id {list} -- the list of books of the library
            books_score {list} --  the list of the books scores

        Returns:
            list -- The books list formed by books objects for the given library
        """
        books = []

        for i in range(len(books_score)):
            if books_score[i].id in books_id:
                books.append(books_score[i])
                books.sort(key=lambda x: x.score, reverse=True)  # sort the books in descending order

        return books

    def create_books(self, books_scores):
        """Create the array of Books objects

        Arguments:
            books {list} -- the list of books individual score

        Returns:
            list -- The books list formed by books objects
        """
        books = []

        for i in range(len(books_scores)):
            books.append(Book(i, books_scores[i]))

        return books

    def parse_hash_code_file(self):
        """
            Parsing the input data

            Returns:
                tuple -- d: the number of days, libraries: the list containing the libraries objects
        """
        file = open("scenarios/{}".format(self.file_path))
        b, l, d = map(int, file.readline().split())  # number of different books, number of libraries, number of days
        book_scores = list(map(int, file.readline().split()))  # scores of the individual books
        books_obj = self.create_books(book_scores)  # from the books_scores create an array of books objects
        libraries = []

        # Get the libraries data
        for i in range(l):
            n, t, m = map(int, file.readline().split())
            books_id = list(map(int, file.readline().split()))  # the books id of the library
            books = self.create_books_list(books_id, books_obj)  # create the library's books list
            libraries.append(Library(i, n, t, m, books))

        return d, libraries
