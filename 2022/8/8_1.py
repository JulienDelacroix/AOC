import sys
import numpy as np

grid = np.array([[c for c in l] for l in sys.stdin.read().splitlines()])
H, W = grid.shape

inside_count = 0
for y in range(1, H-1):
    for x in range(1, W-1):
        arround = [ grid[y,:x], grid[y,x+1:], grid[:y,x], grid[y+1:,x] ]
        inside_count += any(max(v) < grid[y][x] for v in arround)

print(inside_count + 2*W + 2*H - 4)
