import sys
import re

TIME = 1000

particles = []
remaining = set()
for n, line in enumerate(sys.stdin.read().splitlines()):
    particles.append(list(map(lambda x : list(map(int, x.split(","))), re.findall("p=<(.+)>, v=<(.+)>, a=<(.+)>", line)[0])))
    remaining.add(n)

for t in range(TIME):
    pos_map = {}
    colliding = set()
    for r in remaining:
        for d in range(3):
            p = particles[r]
            p[1][d] += p[2][d]
            p[0][d] += p[1][d]
        rpos = tuple(p[0])
        if rpos in pos_map:
            colliding.add(r)
            colliding.add(pos_map[rpos])
        else:
            pos_map.update({rpos : r})
    remaining -= colliding

print(len(remaining))
