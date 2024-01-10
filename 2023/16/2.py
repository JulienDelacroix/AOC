import sys

next_direction = {
    '|' : [[0], [0, 2], [2], [0, 2]],
    '-' : [[1, 3], [1], [1, 3], [3]],
    '/' : [[1], [0], [3], [2]],
    '\\' : [[3], [2], [1], [0]],
    '.' : [[0], [1], [2], [3]]
}

def nextPos(p, dir):
    x, y = p
    return ((x, y-1), (x+1, y), (x, y+1), (x-1, y))[dir]

def energized(x, y, d):
    photons = set()
    photons.add(((x, y), d))

    visited = set()
    while len(photons):
        next_photons = set()
        for p in photons:
            pos, dir = p
            visited.add((pos, dir))
            for ndir in next_direction[grid[pos]][dir]:
                npos = nextPos(pos, ndir)
                if npos in grid and (npos, ndir) not in visited:
                    next_photons.add((npos, ndir))
        photons = next_photons

    return len(set(p for p, _ in visited))


grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})

res = 0
xmax = max(p[0] for p in grid.keys())
ymax = max(p[1] for p in grid.keys())
for x in range(xmax+1):
    res = max(res, energized(x, 0, 2))
    res = max(res, energized(x, ymax, 0))
for y in range(ymax + 1):
    res = max(res, energized(0, y, 1))
    res = max(res, energized(xmax, y, 3))

print(res)
