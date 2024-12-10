import sys

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})
        if c == '^':
            start_pos = (x, y)

DIRS = ">v<^"
DIR_OFFSETS = ((1, 0), (0, 1), (-1, 0), (0, -1))

def cw(dir):
    return (dir + 1) % 4

def next_pos(pos, dir):
    x, y = pos
    dx, dy = DIR_OFFSETS[dir]
    return (x + dx, y + dy)
        
visited = set()
pos, dir = start_pos, DIRS.index('^')
while pos in grid:
    visited.add(pos)
    npos = next_pos(pos, dir)
    if npos in grid and grid[npos] == '#':
        dir = cw(dir)
    else:
        pos = npos

print(len(visited))
