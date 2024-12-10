import sys

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})
        if c == '^':
            start = (x, y)

DIRS = ">v<^"
DIR_OFFSETS = ((1, 0), (0, 1), (-1, 0), (0, -1))

def cw(dir):
    return (dir + 1) % 4

def next_pos(pos, dir):
    x, y = pos
    dx, dy = DIR_OFFSETS[dir]
    return (x + dx, y + dy)

def simulate(grid, start_pos, block_pos):
    visited_states = set()
    pos, dir = start_pos, DIRS.index('^')
    while pos in grid:
        if (pos, dir) in visited_states:
            return None
        visited_states.add((pos, dir))

        npos = next_pos(pos, dir)
        if npos in grid and (grid[npos] == '#' or npos == block_pos):
            dir = cw(dir)
        else:
            pos = npos

    return set(pos for pos, _ in visited_states)

visited = simulate(grid, start, None)
print(sum(not simulate(grid, start, block) for block in visited if block != start))
