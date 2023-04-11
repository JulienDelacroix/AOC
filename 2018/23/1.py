import sys
import re

def manhattan(bot1, bot2):
    return sum(abs(v2-v1) for v1, v2 in zip(bot1[:3], bot2[:3]))

bots = []
for line in sys.stdin.read().splitlines():
    x, y, z, r = map(int, re.findall("(-?\d+)", line))
    bots.append((x, y, z, r))

strongest = max(bots, key=lambda v: v[3])
print(sum(manhattan(strongest, b) <= strongest[3] for b in bots))
