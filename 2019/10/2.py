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

_, best = max((len(l), a) for a, l in visible.items())

targets = defaultdict(list)
for target in asteroids:
    if target != best:
        s = step(best, target)
        targets[s].append(target)

sortable_targets = []
for s in targets.keys():
    targets[s].sort(key = lambda v: abs(v[0]-best[0]))
    for n, t in enumerate(targets[s]):
        # Initially angle = atan2(dy, dx)
        # flip arround x axis: (x, y) => (x, -y): now angle = atan2(-dy, dx)
        # counter clockwise rotation of PI/2 (x, y) -> (-y, x): now angle = atan2(dx, dy)
        # sort by decreasing angle: angle = -atan2(dx, dy)
        angle = -math.atan2(t[0]-best[0], t[1]-best[1])
        sortable_targets.append((n, angle, t))

last = sorted(sortable_targets)[199][2]
print(last[0] * 100 + last[1])
