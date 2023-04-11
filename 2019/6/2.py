import sys
from collections import defaultdict
import networkx as nx

graphdesc = defaultdict(list)
for line in sys.stdin.read().splitlines():
    center, orbiting = line.split(")")
    graphdesc[center].append(orbiting)
    graphdesc[orbiting].append(center)

g = nx.Graph(graphdesc)
print(nx.shortest_path_length(g, "YOU", "SAN") - 2)
