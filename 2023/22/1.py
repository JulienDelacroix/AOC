import sys
from collections import defaultdict

def horizontalSlice(b):
    for x in range(b[0][0], b[1][0] + 1):
        for y in range(b[0][1], b[1][1] + 1):
            yield(x, y)

bricks = []
for line in sys.stdin.read().splitlines():
    s1, s2 = line.split("~")
    start = tuple(map(int, s1.split(",")))
    end = tuple(map(int, s2.split(",")))
    bricks.append((start, end))

bricks.sort(key = lambda b : b[0][2])

supporting = {}
top = defaultdict(lambda: (0, None))
for b in bricks:
    z_intersect = max(top[pos][0] for pos in horizontalSlice(b))
    supporting.update({b : set(top[pos][1] for pos in horizontalSlice(b) if top[pos][0] == z_intersect)})

    new_zmax = z_intersect + 1 + (b[1][2] - b[0][2])
    top.update({pos : (new_zmax, b) for pos in horizontalSlice(b)})

critical_bricks = set({next(iter(s)) for s in supporting.values() if(len(s)) == 1}) - set({None})
print(len(bricks) - len(critical_bricks))
