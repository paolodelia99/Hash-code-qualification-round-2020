import sys
from pathlib import Path
from scenarioParser import ScenarioParser


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


class Book:
    """
    A class representing the book
    """

    def __init__(self, id, score):
        self.id = id
        self.score = score


def create_books(books_scores):
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


def main():
    """Main entry
    """
    scenario_code_name = sys.argv[1]  # read scenario from the command line
    scenario_parser = ScenarioParser(scenario_code_name)
    days, libraries = scenario_parser.parse_hash_code_file()
    solve(scenario_code_name, days, libraries)


def solve(scenario, days, libraries):
    # sorting the libraries by the total score in descending order
    libraries.sort(key=lambda x: x.tot_score, reverse=True)

    tot_sign_up = 0  # stores the total sign up time for the chosen libraries
    sign_up_lib = []  # list that stores the library chosen for the sign up process in order
    books_shipped = []  # list of tuple containing the books id shipped per day for library

    # select the right libraries
    for lib in libraries:
        if tot_sign_up + lib.sign_up_time <= days:
            tot_sign_up += lib.sign_up_time
            sign_up_lib.append(lib)
            books_shipped.append(get_best_books(lib, books_shipped, days, tot_sign_up))
        else:
            break

    write_solution(scenario, sign_up_lib, books_shipped)


def get_best_books(lib, assigned_books, days, tot_sign_up):
    """
        Returns the best book of the given library based
        on the previous choices

        Arguments:
            lib {Library} the chosen library object
            assigned_books {list} the list of the books already chosen
            days {int} tot days
            tot_sign_up {int} the days already assigned to sign up the chosen libraries

        Returns:
            tuple -- representing the best choice for the given library
    """
    if not assigned_books:
        return tuple(book.id for book in lib.books)
    else:
        time = days - tot_sign_up

        set_books = set(list(sum(assigned_books, ())))  # the set of the books already scanned
        set_lib_book = set(book.id for book in lib.books)  # set of the books in the library
        chosen_books = list(set_lib_book.difference(set_books))  # difference between the two sets

        return tuple(chosen_books[:time * lib.book_per_day])


def write_solution(scenario, sign_up, books_shipped):
    # Get the scenario name
    scenario = scenario.split(".")
    scenario = scenario[0]

    file_name = f"{scenario}.solution.txt"
    abs_path = Path().absolute()
    file_path = f"{abs_path}/solved/{file_name}"

    # check if the file already exists, if it does then delete it
    my_file = Path(file_path)
    if my_file.is_file():
        my_file.unlink()

    # Create a new file
    file = open(file_path, "w")
    file.write(str(len(sign_up)) + "\n")
    for i in range(len(sign_up)):
        file.write("{} {} \n".format(sign_up[i].id, sign_up[i].no_books))
        for j in books_shipped[i]:  # printing the books
            file.write(str(j) + " ")
        file.write("\n")


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


def parse_data(file_to_read):
    """
        Parsing the input data

        Returns:
            tuple -- d: the number of days, libraries: the list containing the libraries objects
    """
    file = open("scenarios/{}".format(file_to_read))
    b, l, d = map(int, file.readline().split())  # number of different books, number of libraries, number of days
    book_scores = list(map(int, file.readline().split()))  # scores of the individual books
    books_obj = create_books(book_scores)  # from the books_scores create an array of books objects
    libraries = []

    # Get the libraries data
    for i in range(l):
        n, t, m = map(int, file.readline().split())
        books_id = list(map(int, file.readline().split()))  # the books id of the library
        books = create_books_list(books_id, books_obj)  # create the library's books list
        libraries.append(Library(i, n, t, m, books))

    return d, libraries


if __name__ == "__main__":
    main()
