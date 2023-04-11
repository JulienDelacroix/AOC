import sys

ITER = 10000

infected = set()
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c == '#':
            infected.add((x,y))

dir = 0
pos = (y//2, y//2)
res = 0
for _ in range(ITER):
    if pos in infected:
        dir = (dir + 1) % 4
        infected.remove(pos)
    else:
        dir = (dir + 3) % 4
        infected.add(pos)
        res += 1
    x, y = pos
    pos = ((x, y-1), (x+1, y), (x, y+1), (x-1, y))[dir]

print(res)