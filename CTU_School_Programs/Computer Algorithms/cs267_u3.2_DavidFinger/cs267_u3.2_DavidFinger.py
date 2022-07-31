from collections import defaultdict

class Graph():
    def __init__(self):

        self.paths = defaultdict(list)
        self.weights = {}

    def add_path(self, fromN, toN, weight):
        self.paths[fromN].append(toN)
        self.paths[toN].append(fromN)
        self.weights[(fromN, toN)] = weight
        self.weights[(toN, fromN)] = weight

graph = Graph()

paths = [
    ('a', 'b', 4),
    ('a', 'c', 2),
    ('b', 'c', 1),
    ('b', 'd', 5),
    ('c', 'd', 8),
    ('c', 'e', 10),
    ('d', 'e', 2),
    ('d', 'z', 6),
    ('e', 'z', 5)
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
        weight = graph.weight[(current, nextN)] + weighttocurrent
        if nextN not in shortest:
            shortest[nextN] = (current, weight)
        else:
            currentshortest = shortest[nextN][1]
            if currentshortest > weight:
                shortest[nextN] = (current, weight)

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

dijsktra(graph, 'z', 'a')
