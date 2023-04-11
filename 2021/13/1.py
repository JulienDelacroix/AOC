import sys
import re

points = set()
points_lines, fold_lines = sys.stdin.read().split("\n\n")
for line in points_lines.splitlines():
    points.add(tuple(map(int, line.strip().split(","))))

for line in fold_lines.splitlines():
    new_points = set()
    axis, pos = re.findall("fold along ([xy])=(\d+)", line)[0]
    if axis=="x":
        x = int(pos)
        for p in points:
            new_points.add(p if p[0] < x else (2 * x - p[0], p[1]))
    if axis=="y":
        y = int(pos)
        for p in points:
            new_points.add(p if p[1] < y else (p[0], 2 * y - p[1]))
    points = new_points
    print(len(points))
    break;
