from library import Library
from book import Book
import os.path


class ScenarioParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def parse_hash_code_file(self):
        """
            Parsing the input data

            Returns:
                tuple -- d: the number of days, libraries: the list containing the libraries objects
        """
        path = "scenarios/{}.txt".format(self.file_path)

        # Check if the path exists
        if not os.path.isfile(path):
            raise Exception('Didn\'t found the file: {}'.format(path))

        b, l, d = None, None, None
        book_scores, books_obj = [], []
        n, t, m = None, None, None
        libraries = []

        with open(path) as fp:
            cnt = 0
            for i, line in enumerate(fp):
                if line == '\n':
                    continue

                if i == 0:
                    b, l, d = line.strip().split(' ')
                elif i == 1:
                    book_scores = list(line.strip().split(' '))
                    books_obj = self.create_books(book_scores)  # from the books_scores create an array of books objects
                elif i % 2 == 0:
                    n, t, m = line.strip().split(' ')
                else:
                    lib_books = list(line.strip().split(' '))
                    books = self.create_books_list(lib_books, books_obj)  # create the library's books list
                    libraries.append(Library(cnt, int(n), int(t), int(m), books))
                    cnt += 1

        return int(d), books_obj, libraries

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
            if str(books_score[i].id) in books_id:
                books.append(books_score[i])
                books.sort(key=lambda x: x.score, reverse=True)  # sort the books in descending order

        return books

    @staticmethod
    def create_books(books_scores):
        """Create the array of Books objects

        Arguments:
            books {list} -- the list of books individual score

        Returns:
            list -- The books list formed by books objects
        """
        books = []

        for i in range(len(books_scores)):
            books.append(Book(i, int(books_scores[i])))

        return books
