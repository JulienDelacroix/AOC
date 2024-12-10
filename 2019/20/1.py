import sys
import string
import networkx as nx
from queue import Queue

# read grid
grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})

# find portals
portals = {}
for pos, c in grid.items():
    if c in string.ascii_uppercase:
        x, y = pos
        if(x+1, y) in grid and grid[(x+1, y)] in string.ascii_uppercase:
            portal = "".join([c, grid[(x+1, y)]])
            if(x+2, y) in grid and grid[(x+2, y)] == '.':
                portals.update({ (x+2, y) : portal })
            else:
                portals.update({ (x-1, y) : portal })
        elif(x, y+1) in grid and grid[(x, y+1)] in string.ascii_uppercase:
            portal = "".join([c, grid[(x, y+1)]])
            if(x, y+2) in grid and grid[(x, y+2)] == '.':
                portals.update({ (x, y+2) : portal })
            else:
                portals.update({ (x, y-1) : portal })

# build graph
def n4(pos): 
    x, y = pos
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)

g = nx.Graph()
def fillGraph(source, dest_list):
    visited = set()
    q = Queue()
    q.put((source, 0))
    visited.add(source)
    while not q.empty():
        pos, dist = q.get()
        if pos != source and pos in dest_list:
            g.add_edge(source, pos, weight=dist)
        else:
            for npos in n4(pos):
                if npos in grid and grid[npos] == '.' and npos not in visited:
                    visited.add(npos)
                    q.put((npos, dist+1))
            
for source in portals.keys():
    fillGraph(source, portals.keys())

# add warps
for t1 in portals.keys():
    if portals[t1] == "AA":
        start_pos = t1
    if portals[t1] == "ZZ":
        dest_pos = t1
    for t2 in portals.keys():
        if t1 != t2 and portals[t1] == portals[t2]:
            g.add_edge(t1, t2, weight=1)

# SSSP
print(nx.shortest_path_length(g, source=start_pos, target=dest_pos, weight="weight"))
