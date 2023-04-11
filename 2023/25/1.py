import sys
import networkx as nx
import math

graphdesc = {}
for line in sys.stdin.read().splitlines():
    source, dest_list = line.split(":")
    graphdesc.update({source : list(dest_list.strip().split(" "))})

g = nx.Graph(graphdesc)
g.remove_edges_from(nx.minimum_edge_cut(g))
print(math.prod(map(len, nx.connected_components(g))))
