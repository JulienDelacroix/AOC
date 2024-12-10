import sys
import re

constraints = []
for line in sys.stdin.read().splitlines():
    disc, size, pos = map(int, re.findall(r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).", line)[0])
    constraints.append((size, (size -(disc + pos)) % size))
constraints.append((11, (11 -(len(constraints)+1)) % 11))

constraints.sort()
for x in range(constraints[-1][1], 100000000, constraints[-1][0]):
    if all(x % q == r for q, r in constraints):
        print(x)
        break
