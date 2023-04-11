import sys
import itertools

blocks = sys.stdin.read().split("\n\n")
randomlist = map(int, blocks[0].split(","))

grids = []
for block in blocks[1:]:
    g = []
    for line in block.splitlines():
        g.append([[v, 0] for v in map(int, line.split())])
    grids.append(g)

for r in randomlist:
    for g in grids:
        n = len(g)
        for y in range(n):
            for x in range(n):
                if g[y][x][0] == r:
                    g[y][x][1] = 1
                    if sum(g[y][i][1] for i in range(n)) == n or sum(g[i][x][1] for i in range(n)) == n:
                        unmarked = sum(g[i][j][0] for i, j in itertools.product(range(n), repeat=2) if g[i][j][1] == 0)
                        print(unmarked * r)
                        exit(0)
    