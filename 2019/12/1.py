import sys
import re

moons = []
for line in sys.stdin.read().splitlines():
    moons.append(list(map(int, re.findall("(-?\d+)", line))) + [0]*3)

for _ in range(1000):
    for m1 in moons:
        for m2 in moons:
            for i in range(3):
                m1[3+i] += m1[i] < m2[i]
                m1[3+i] -= m1[i] > m2[i]

    for m in moons:
        for i in range(3):
            m[i] += m[3+i]

print(sum(sum(abs(v) for v in m[:3]) * sum(abs(v) for v in m[3:]) for m in moons))
