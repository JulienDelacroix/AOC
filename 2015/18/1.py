import sys

def n8(pos):
    x, y = pos
    for next_x, next_y in [(x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
        if 0 <= next_x < 100 and 0 <= next_y < 100:
            yield (next_x, next_y)

on = set()
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c == "#": on.add((x, y))

for _ in range(100):
    next_on = set()
    for y in range(100):
        for x in range(100):
            pos = (x, y)
            n = sum(p in on for p in n8((pos)))
            if (pos in on and (n == 2 or n == 3)) or (pos not in on and n == 3) : next_on.add(pos)
    on = next_on

print(len(on))
