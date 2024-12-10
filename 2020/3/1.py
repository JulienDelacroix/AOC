import sys

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})

xmax = max(pos[0] for pos in grid.keys())

res = 0
x, y = 0, 0
while (x, y) in grid:
    res += grid[(x, y)] == '#'
    x = (x + 3) % (xmax + 1)
    y = y + 1

print(res)
