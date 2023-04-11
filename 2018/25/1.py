import sys
import networkx as nx

points = []
res = 0

g = nx.Graph()
for line in sys.stdin.read().splitlines():
    p1 = tuple(map(int, line.split(",")))

    g.add_node(p1)
    for p2 in points:
        if sum(abs(v2 - v1) for v1, v2 in zip(p1, p2)) <= 3:
            g.add_edge(p1, p2)
    points.append(p1)

print(len(list(nx.connected_components(g))))
