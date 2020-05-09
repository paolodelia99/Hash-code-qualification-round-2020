import sys
from parsers.scenarioParser import ScenarioParser
from parsers.solutionParser import SolutionParser


def check_solution_validity(days:int, libraries:list, books:list) -> int:
    """

    @param days: the day for the sign up process
    @param libraries: the libraries of the scenario
    @param books: the books of the scenario
    @return: the total score of the solution
    """
    try:
        sol_parser = SolutionParser(file, days, libraries, books)
        tot_score = sol_parser.parse_solution_file()

        return tot_score
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

    tot_score = check_solution_validity(days, libraries, books)

    print('Your solution have scored {} points'.format(tot_score))
    print('The maximum score possible is {}'.format(max_score))
except Exception as exception:
    print(exception)
