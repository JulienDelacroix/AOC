import sys 

def dist(p1, p2): return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

points = set()
for line in sys.stdin.read().splitlines():
    x, y = map(int, line.split(","))
    points.add((x, y))

xmax = max(p[0] for p in points)
ymax = max(p[1] for p in points)

owners = {}
borders = set()
for x in range(xmax+1):
    for y in range(ymax+1):
        mindist = min(dist((x, y), p) for p in points)
        for p in points:
            if dist((x, y), p) == mindist:
                owners.update({(x, y) : None if (x, y) in owners else p })
        if x in (0, xmax) or y in(0, ymax):
            borders.add(owners[(x, y)])

print(max(sum(o == p for p in owners.values()) for o in points - borders))
