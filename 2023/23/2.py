import sys
import functools
from collections import defaultdict
from queue import Queue

grid = {}
targets = defaultdict(list)

def n4(pos): 
    x, y = pos
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)

def computeDist(source, dest_list):
    visited = set()
    q = Queue()
    q.put((source, 0))
    visited.add(source)
    while not q.empty():
        pos, dist = q.get()
        if pos in dest_list:
            targets[source].append((pos, dist))
        else:
            for npos in n4(pos):
                if npos in grid and grid[npos] != '#' and npos not in visited:
                    visited.add(npos)
                    q.put((npos, dist+1))

@functools.lru_cache(None)
def solve(pos, remaining, depth):
    if pos == goal: return 0
    
    res = None
    for t, d in targets[pos]:
        if t in remaining:
            found = solve(t, remaining - frozenset({t}), depth+1)
            if found is not None:
                res = (d + found) if res == None else max(res, d + found)
    return res

# read grid
lines = sys.stdin.read().splitlines()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})

# compute checkpoints and targets/distances
start = (lines[0].index('.'), 0)
goal = (lines[-1].index('.'), len(lines)-1)
checkpoints = set([start, goal])
checkpoints |= set(c for c in grid.keys() if grid[c] != '#' and sum(p in grid and grid[p] != '#' for p in n4(c)) > 2)
for c in checkpoints:
    computeDist(c, checkpoints - {c})

print(solve(start, frozenset(checkpoints) - frozenset({start}), 0))
