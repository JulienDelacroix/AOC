import sys

tracked, overlap = set(), set()

for line in sys.stdin.read().splitlines():
    points = line.split("->")
    x1, y1 = map(int, points[0].split(","))
    x2, y2 = map(int, points[1].split(","))

    (tracked if (x1, y1) not in tracked else overlap).add((x1, y1))
    while x1 != x2 or y1 != y2:
        if x1 != x2: x1 = x1 + (x2-x1) // abs(x2-x1)
        if y1 != y2: y1 = y1 + (y2-y1) // abs(y2-y1)
        (tracked if (x1, y1) not in tracked else overlap).add((x1, y1))

print(len(overlap))
