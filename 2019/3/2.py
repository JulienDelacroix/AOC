import sys

steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]

elapsed = {}
pathes = [set(), set()]
for n, line in enumerate(sys.stdin.read().splitlines()):
    x, y, t = 0, 0, 0
    for move in line.split(","):
        direction, distance = "RDLU".index(move[0]), int(move[1:])
        step = steps[direction]
        for _ in range(distance):
            t += 1
            x, y = x + step[0], y + step[1]
            pathes[n].add((x, y))
            if (n, x, y) not in elapsed:
                elapsed.update({(n, x, y) : t})

print(min((elapsed[(0, *pos)] + elapsed[(1, *pos)]) for pos in (pathes[0] & pathes[1])))
