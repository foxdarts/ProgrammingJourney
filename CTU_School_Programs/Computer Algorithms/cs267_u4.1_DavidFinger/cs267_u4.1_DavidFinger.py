from collections import defaultdict

class Graph():
    def __init__(self):

        self.paths = defaultdict(list)
        self.weights = {}

    def add_path(self, fromN, toN, weights):
        self.paths[fromN].append(toN)
        self.paths[toN].append(fromN)
        self.weights[(fromN, toN)] = weights
        self.weights[(toN, fromN)] = weights

graph = Graph()

paths = [
    ('10', '14', 4),
    ('14', '19', 5),
    ('14', '27', 13),
    ('27', '35', 8),
    ('35', '31', 4),
    ('42', '35', 7),
]

for path in paths:
    graph.add_path(*path)

def dijsktra(graph, start, end):
    shortest = {start: (None, 0)}
    current = start
    explored = set()

    while current != end:
        explored.add(current)
        destination = graph.paths[current]
        weighttocurrent = shortest[current][1]

    for nextN in destination:
        weights = graph.weights[(current, nextN)] + weighttocurrent
        if nextN not in shortest:
            shortest[nextN] = (current, weights)
        else:
            currentshortest = shortest[nextN][1]
            if currentshortest > weights:
                shortest[nextN] = (current, weights)

    nextdestination = {node: shortest[node] for node in shortest if node not in explored}
    if not nextdestination:
        return "route unfeasible"

    current = min(nextdestination, key=lambda k: nextdestination[k][1])

    route = []
    while current is not None:
        route.append(current)
        nextN = shortest[current][0]
        current = nextN

    route = route[::-1]

    return route

dijsktra(graph, '42', '10')
