from owlready2 import *


def addInstances(onto):
    # Another small tournament
    pesho = onto.Player("Pesho")
    gosho = onto.Player("Gosho")

    tournament = onto.Locals("PlovdivLocals06.02.2022")

    r1 = onto.Round()

    m1 = onto.Match()

    m1.has_players = [pesho, gosho]
    m1.has_winner = gosho
    r1.has_matches = [m1]

    pesho.has_points = 3
    gosho.has_points = 0

    tournament.has_rounds = [r1]

    c1 = onto.NormalTrap()
    c2 = onto.ContiniousTrap()
    c3 = onto.ContiniousTrap()
    d1 = onto.Deck(name="Eldlich", archtype=[
                   "trap deck", "eldlich"], has_cards=[c1, c2, c3])

    pesho.uses = d1


def executeQuery(worldBR):
    # Reading file with queries in a single string
    with open("SPARQL_queries.rq", "r") as read_file:
        data = read_file.read()

    # Tokenize string on the basis of regex for extracting queries
    queries = re.split('#.*', data)

    for i in range(1, len(queries)):
        print("----------{}".format(queries[i]), end='')
        result = list(default_world.sparql(queries[i]))
        resultBR = list(worldBR.sparql(queries[i]))
        print("result =\n{}".format(result))
        print("result before reasoning =\n{}\n----------".format(resultBR))
