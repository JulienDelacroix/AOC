import sys
from functools import reduce
import operator

digits = {}
symbols = set()

def n8(pos):
    x, y = pos
    for next_x, next_y in [(x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
        yield (next_x, next_y)

for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c.isdigit():
            digits.update({ (x,y) : c })
        elif c != '.':
            symbols.add((x, y))

res = 0
for s in symbols:
    found = {}
    for nx, ny in n8(s):
        xstart = xend = nx
        while (xstart, ny) in digits: xstart -= 1
        while (xend, ny) in digits: xend += 1
        if xstart != xend:
            v = int("".join(digits[(x, ny)] for x in range(xstart+1, xend)))
            found.update({(xstart+1, ny) : v})
    
    if len(found) == 2:
        res += reduce(operator.mul, found.values(), 1)

print(res)
