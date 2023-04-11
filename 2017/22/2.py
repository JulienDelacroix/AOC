import sys

ITER = 10000000

# states:  0 = clean, 1 = weakened, 2 = infected, 3 = flagged
states = {}

for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c == '#':
            states.update({(x,y) : 2})

dir = 0
pos = (y//2, y//2)
res = 0

for _ in range(ITER):
    s = states.get(pos, 0)
    res += (s == 1)
    dir = (dir + (3, 0, 1, 2)[s]) % 4
    states.update({pos : (s+1) %  4})
    
    x, y = pos
    pos = ((x, y-1), (x+1, y), (x, y+1), (x-1, y))[dir]

print(res)