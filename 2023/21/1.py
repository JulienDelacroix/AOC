import sys

def n4(pos):
    x, y = pos
    for ox, oy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        yield (x + ox, y + oy)

reachable = set()
grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c == 'S':
            reachable.add((x, y))
            c = '.'
        grid.update({(x, y) : c})

STEPS = 64
for _ in range(STEPS):
    next_reachable = set()
    for pos in reachable:
        for npos in n4(pos):
            if npos in grid and grid[npos] == '.':
                next_reachable.add(npos)
    reachable = next_reachable
    print(_, len(reachable))

print(len(reachable))
