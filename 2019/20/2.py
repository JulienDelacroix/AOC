import sys
import string
import networkx as nx
from queue import Queue

# read grid
grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})

xmax = max(pos[0] for pos in grid.keys())
ymax = max(pos[1] for pos in grid.keys())

# find portals
portals = {}
for (x, y), c in grid.items():
    if c in string.ascii_uppercase:
        if(x+1, y) in grid and grid[(x+1, y)] in string.ascii_uppercase:
            portal = "".join([c, grid[(x+1, y)]])
            if(x+2, y) in grid and grid[(x+2, y)] == '.':
                portals.update({ (x+2, y) : (portal, x == 0) })
            else:
                portals.update({ (x-1, y) : (portal, x+1 == xmax) })
        elif(x, y+1) in grid and grid[(x, y+1)] in string.ascii_uppercase:
            portal = "".join([c, grid[(x, y+1)]])
            if(x, y+2) in grid and grid[(x, y+2)] == '.':
                portals.update({ (x, y+2) : (portal, y == 0) })
            else:
                portals.update({ (x, y-1) : (portal, y+1 == ymax) })

MAX_LEVEL = 100

# build graph
def n4(pos): 
    x, y = pos
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)

g = nx.DiGraph()
def fillGraph(source, dest_list):
    visited = set()
    q = Queue()
    q.put((source, 0))
    visited.add(source)
    while not q.empty():
        pos, dist = q.get()
        if pos != source and pos in dest_list:
            for d in range(MAX_LEVEL):
                g.add_edge((portals[source], d), (portals[pos], d), weight=dist)
        else:
            for npos in n4(pos):
                if npos in grid and grid[npos] == '.' and npos not in visited:
                    visited.add(npos)
                    q.put((npos, dist+1))
            
for source in portals.keys():
    fillGraph(source, portals.keys())

# add warps
for p1 in portals.values():
    if p1[0] == "AA":
        start = p1
    if p1[0] == "ZZ":
        dest = p1
    for p2 in portals.values():
        if p1 != p2 and p1[0] == p2[0]:
            if p1[1]: #outer portal
                for d in range(1, MAX_LEVEL):
                    g.add_edge((p1, d), (p2, d-1), weight=1)
            else:
                for d in range(0, MAX_LEVEL):
                    g.add_edge((p1, d), (p2, d+1), weight=1)                    

# SSSP
print(nx.shortest_path_length(g, source=(start, 0), target=(dest, 0), weight="weight"))
