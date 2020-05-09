import sys
from parsers.scenarioParser import ScenarioParser
from parsers.solutionParser import SolutionParser

# TODO read scenario and solution from command line arguments. Verify and compute score


def check_solution_validity(days, libraries, books):
    try:
        sol_parser = SolutionParser(file, days, libraries, books)
        sol_parser.parse_solution_file()
    except Exception as excp:
        print(excp)

"""Main function begins"""
cmd = sys.argv[1:]
assert cmd, "There should be at least one argument"

try:
    file = cmd[0]
    parser = ScenarioParser(file)
    days, books, libraries = parser.parse_hash_code_file()
    max_score = sum([book.score for book in books])

    check_solution_validity(days, libraries, books)
    #fixme
    # - get the books and the library from the scenario DONE
    # - compute the maximum score possible DONE
    # - read and check the validity of the solution
    # - compute the score of the solution comparing it with the max solution
except Exception as exception:
    print(exception)

