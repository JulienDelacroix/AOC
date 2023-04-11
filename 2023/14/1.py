import sys

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})

M = max(v[0] for v in grid.keys()) + 1
res = 0
for x in range(M):
    curr = 0
    for y in range(M):
        if grid[(x, y)] == '#':
            curr = y+1
        elif grid[(x, y)] == 'O':
            res += M-curr
            curr += 1
print(res)
