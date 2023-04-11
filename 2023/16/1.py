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

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})

photons = set()
photons.add(((0, 0), 1))

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

print(len(set (p for p, _ in visited)))
