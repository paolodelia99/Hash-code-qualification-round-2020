import sys
from scenarioParser import ScenarioParser

# TODO read scenario and solution from command line arguments. Verify and compute score

"""Main function begins"""
cmd = sys.argv[1:]
assert cmd, "There should be at least one argument"

try:
    file = open("scenarios/{}".format(cmd[0]))
    #fixme
    # - get the books and the library from the scenario
    # - compute the maximum score possible
    # - read and check the validity of the solution
    # - compute the score of the solution comparing it with the max solution
except:
    raise Exception("Didn't found the scenario file")
finally:
    file.close()
