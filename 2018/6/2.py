import sys 

def dist(p1, p2): return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

points = set()
for line in sys.stdin.read().splitlines():
    x, y = map(int, line.split(","))
    points.add((x, y))

xmax = max(p[0] for p in points)
ymax = max(p[1] for p in points)

res = 0
for x in range(xmax+1):
    for y in range(ymax+1):
        if sum(dist((x, y), p) for p in points) < 10000:
            res += 1
print(res)
