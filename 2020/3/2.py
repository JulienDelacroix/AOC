import sys
import math

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})

xmax = max(pos[0] for pos in grid.keys())

def count_trees(slope):
    res = 0
    x, y = 0, 0
    dx, dy = slope
    while (x, y) in grid:
        res += grid[(x, y)] == '#'
        x = (x + dx) % (xmax + 1)
        y = y + dy
    return res
    
print(math.prod(count_trees(slope) for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
