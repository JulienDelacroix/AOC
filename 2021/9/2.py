import sys
import functools
from queue import Queue

def n4(grid, pos): 
    x, y = pos
    for nextpos in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if nextpos in grid:
            yield nextpos

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : int(c)})

bassins = []
for startpos, h in grid.items():
    if all(h < grid[nextpos] for nextpos in n4(grid, startpos)):
        visited = set()
        q = Queue()
        q.put(startpos)
        visited.add(startpos)
        while not q.empty():
            pos = q.get()
            for nextpos in n4(grid, pos):
                if nextpos not in visited and (9 > grid[nextpos] >= grid[pos]):
                    q.put(nextpos)
                    visited.add(nextpos)
        bassins.append(len(visited))

print(functools.reduce(lambda r, v: r*v, sorted(bassins)[-3:]))
