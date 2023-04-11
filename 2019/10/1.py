import sys
import itertools
import math
from collections import defaultdict

def step(source, dest):
    (x1, y1), (x2, y2) = source, dest
    dx, dy = x2 - x1, y2 - y1
    divisor = math.gcd(x2 - x1, y2 - y1)
    return (dx // divisor, dy // divisor)

visible = defaultdict(set)
asteroids = set()
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c == '#':
            asteroids.add((x, y))

for a1, a2 in itertools.combinations(asteroids, 2):
    s = step(a1, a2)
    visible[a1].add(s)
    visible[a2].add((-s[0], -s[1]))

print(max(len(l) for l in visible.values()))
