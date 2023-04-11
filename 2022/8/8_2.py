import sys
import numpy as np
import math

def visibility(trees, t):
    vl = 0
    for other in trees:
        vl += 1
        if t <= other:
            break
    return vl

grid = np.array([[c for c in l] for l in sys.stdin.read().splitlines()])
H, W = grid.shape

result = 1
for y in range(1, H-1):
    for x in range(1, W-1):
        arround = [ reversed(grid[y,:x]), grid[y,x+1:], reversed(grid[:y,x]), grid[y+1:,x] ]
        result = max(result, math.prod(visibility(v, grid[y][x]) for v in arround))

print(result)
