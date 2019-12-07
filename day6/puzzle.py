import networkx as nx

lines = []
with open("input.txt", "r") as f:
    lines = f.readlines()

test_lines = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""".split("\n")

edges = [x.replace("\n", "").split(")") for x in lines]
sources = set([e[1] for e in edges])

# First puzzle

graph = nx.DiGraph()
for e in edges:
    graph.add_edge(e[1], e[0])

reachable = [len(nx.descendants(graph, s)) for s in sources]
print(sum(reachable))


# Second puzzle
graph = nx.Graph()
for e in edges:
    graph.add_edge(e[0], e[1])
path = nx.shortest_path(graph, "YOU", "SAN")

print(len(path) - 3)
