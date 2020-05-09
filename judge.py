import sys
from parsers.scenarioParser import ScenarioParser
from parsers.solutionParser import SolutionParser


# TODO read scenario and solution from command line arguments. Verify and compute score


def check_solution_validity(days, libraries, books):
    try:
        sol_parser = SolutionParser(file, days, libraries, books)
        tot_score = sol_parser.parse_solution_file()

        return tot_score
    except Exception as excp:
        print(excp)


"""Main function begins"""
cmd = sys.argv[1:]
if False:
    assert cmd, "There should be at least one argument"

try:
    file = "a_example"
    parser = ScenarioParser(file)
    days, books, libraries = parser.parse_hash_code_file()
    max_score = sum([book.score for book in books])

    tot_score = check_solution_validity(days, libraries, books)

    print('Your solution have scored {} points'.format(tot_score))
    print('The maximum score possible is {}'.format(max_score))
except Exception as exception:
    print(exception)
