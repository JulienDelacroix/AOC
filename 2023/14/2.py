import sys

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})

M = max(v[0] for v in grid.keys()) + 1

step = 0
remaining = 1000000000
visited = {}
while remaining:
    for _ in range(4):
        next_grid = {}
        for x in range(M):
            curr = 0
            for y in range(M):
                if (x, y) in grid:
                    if grid[(x, y)] == '#':
                        next_grid.update({(M-1-y, x): '#'})
                        curr = y+1
                    elif grid[(x, y)] == 'O':
                        next_grid.update({(M-1-curr, x): 'O'})
                        curr += 1
        grid = next_grid

    step += 1
    remaining -= 1
    key = tuple(grid)
    if key not in visited:
        visited.update({key : step})
    else:
        cycle_len = step - visited[key]
        remaining = remaining % cycle_len

print(sum(M-y for (_, y), c in grid.items() if c == 'O'))
