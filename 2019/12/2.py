import sys
import re
import math

moons = []
for line in sys.stdin.read().splitlines():
    moons.append(list(map(int, re.findall(r"(-?\d+)", line))) + [0]*3)

visited = set()
cycles =  [None] * 3

for step in range(10000000):
    for m1 in moons:
        for m2 in moons:
            for i in range(3):
                m1[3+i] += m1[i] < m2[i]
                m1[3+i] -= m1[i] > m2[i]

    for index, m in enumerate(moons):
        for i in range(3):
            m[i] += m[3+i]

    for i in range(3):
        state = (i, tuple((m[i], m[3+i]) for m in moons))
        if state in visited and cycles[i] is None: 
            cycles[i] = step
        visited.add((state))
    
    if all(v != None for v in cycles):
        break
    
print(math.lcm(*cycles))
