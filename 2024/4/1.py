import sys

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})

def next(pos, dir):
    x, y = pos
    return [(x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1)][dir]

def word(pos, dir):
    w = []
    for _ in range(4):
        if pos in grid:
            w.append(grid[pos])
            pos = next(pos, dir)
    return w

def xmas(pos):
    return sum(word(pos, dir) == ['X', 'M', 'A', 'S'] for dir in range(8)) if grid[pos] == 'X' else 0

print(sum(xmas(pos) for pos in grid.keys()))
