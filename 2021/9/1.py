import sys

def n4(grid, pos): 
    x, y = pos
    for nextpos in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if nextpos in grid:
            yield nextpos

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : int(c)})

res = 0
for pos, h in grid.items():
    if all(h < grid[nextpos] for nextpos in n4(grid, pos)):
        print(pos, h)
        res += (h + 1)

print(res)
