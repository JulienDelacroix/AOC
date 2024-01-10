import sys
import math

up = 0
right = 1
down = 2
left = 3

nextDir = {
    '|' : (up, None, down, None),
    '-': (None, right, None, left),
    'L': (None, None, right, up),
    'J': (None, up, left, None),
    '7' : (left, down, None, None),
    'F' : (right, None, None, down),
    '.' : (None, None, None, None)
}

def nextPos(p, dir):
    x, y = p
    return ((x, y-1), (x+1, y), (x, y+1), (x-1, y))[dir]

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c == 'S':
            start = (x, y)
        grid.update({(x, y) : c})

loop = [start]
vertices = [ start]
dir = next(d for d in range(4) if nextDir[grid[nextPos(start, d)]][d])
pos = nextPos(start, dir)

while pos != start:
    loop.append(pos)
    if grid[pos] in "LJ7F":
        vertices.append(pos)
    dir = nextDir[grid[pos]][dir]    
    pos = nextPos(pos, dir)

area = abs(sum(x1 * y2 - y1 * x2 for (x1, y1), (x2, y2) in zip(vertices, vertices[1:] + [vertices[0]])) / 2)
print(int(area - len(loop) / 2 + 1))
