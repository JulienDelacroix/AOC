import sys

galaxies = []
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c == '#':
            galaxies.append((x, y))

xMax = max(g[0] for g in galaxies)
yMax = max(g[1] for g in galaxies)

xVoid = set(x for x in range(xMax) if all(g[0] != x for g in galaxies))
yVoid = set(y for y in range(yMax) if all(g[1] != y for g in galaxies))

total = 0
for source in galaxies:
    for dest in galaxies:
        total += sum(1000000 if x in xVoid else 1 for x in range(*sorted([source[0], dest[0]])))
        total += sum(1000000 if y in yVoid else 1 for y in range(*sorted([source[1], dest[1]])))

print(total/2)
