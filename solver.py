import sys
from pathlib import Path
from parsers import scenarioParser


def main():
    """Main entry
    """
    try:
        scenario_code_name = sys.argv[1]  # read scenario from the command line
        scenario_parser = scenarioParser.ScenarioParser(scenario_code_name)
        days, books, libraries = scenario_parser.parse_hash_code_file()
        solve(scenario_code_name, days, libraries)
    except Exception as exc:
        print(exc)


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


if __name__ == "__main__":
    main()
