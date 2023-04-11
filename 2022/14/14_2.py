
import sys
from collections import defaultdict

grid = defaultdict(int)

for line in sys.stdin.read().splitlines():
    path = [ tuple(map(int, token.split(","))) for token in line.split("->") ]
    for (x1, y1), (x2, y2) in zip(path, path[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])        
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[(x, y)] = 1
            
y_max = max(y for (_, y) in grid.keys())

sand = 0
path = [(500, 0)]
while path:
    (x, y) = path[-1]

    if grid[(x, y+1)] == 0 and y <= y_max:
        path.append((x, y+1))
    elif grid[(x-1, y+1)] == 0 and y <= y_max:
        path.append((x-1, y+1))
    elif grid[(x+1, y+1)] == 0 and y <= y_max:
        path.append((x+1, y+1))
    else:
        sand += 1
        grid[(x, y)] = 1
        path.pop()

print(sand)
