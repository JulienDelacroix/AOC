import sys
from collections import defaultdict
import networkx as nx

graphdesc = defaultdict(list)
for line in sys.stdin.read().splitlines():
    center, orbiting = line.split(")")
    graphdesc[center].append(orbiting)

g = nx.Graph(graphdesc)
print(sum(len(path)-1 for _, path in nx.single_source_shortest_path(g, "COM").items()))
