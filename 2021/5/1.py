import sys

tracked, overlap = set(), set()

for line in sys.stdin.read().splitlines():
    points = line.split("->")
    x1, y1 = map(int, points[0].split(","))
    x2, y2 = map(int, points[1].split(","))

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            (tracked if (x1, y) not in tracked else overlap).add((x1, y))
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            (tracked if (x, y1) not in tracked else overlap).add((x, y1))

print(tracked, overlap, len(overlap))
