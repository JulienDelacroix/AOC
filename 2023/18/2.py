import sys
import re

x = y = 0
vertices = [(x, y)]
total_dist = 0
for line in sys.stdin.read().splitlines():
    _, _, color = re.findall("(\w) (\d+) \(#(\w+)\)", line)[0]
    dist = int(color[:5], 16)
    dir = int(color[5])

    x += (1, 0, -1, 0)[dir] * int(dist)
    y += (0, 1, 0, -1)[dir] * int(dist)
    total_dist += int(dist)
    vertices.append((x, y))

area = abs(sum(x1 * y2 - y1 * x2 for (x1, y1), (x2, y2) in zip(vertices[:-1], vertices[1:])) / 2)
print(int(area + total_dist/2 + 1))
