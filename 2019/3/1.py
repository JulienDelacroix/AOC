import sys

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]

pathes = [set(), set()]
for n, line in enumerate(sys.stdin.read().splitlines()):
    x, y = 0, 0
    for move in line.split(","):
        direction, distance = "RDLU".index(move[0]), int(move[1:])
        step = steps[direction]
        for _ in range(distance):
            x, y = x + step[0], y + step[1]
            pathes[n].add((x, y))

print(min(sum(abs(v) for v in pos) for pos in (pathes[0] & pathes[1])))
