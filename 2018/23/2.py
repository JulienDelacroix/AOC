import sys
import re
from queue import PriorityQueue

def dist_from_box(box, pos):
    dist = 0
    for i in range(3):
        bstart, bend = box[0][i], box[1][i] - 1
        if  pos[i] < bstart: dist += (bstart - pos[i])
        if  pos[i] > bend: dist += (pos[i] - bend)
    return dist

def split(box):
    (x1, y1, z1), (x2, y2, z2) = box
    mx, my, mz = (x1 + x2) // 2, (y1 + y2) // 2, (z1 + z2) // 2
    for xstart, xend in [(x1, mx), (mx, x2)]:
        for ystart, yend in [(y1, my), (my, y2)]:
            for zstart, zend in [(z1, mz), (mz, z2)]:
                yield ((xstart, ystart, zstart), (xend, yend, zend))
   
bots = []
for line in sys.stdin.read().splitlines():
    x, y, z, r = map(int, re.findall("(-?\d+)", line))
    bots.append((x, y, z, r))

bigbox = (tuple(min(b[i] for b in bots) for i in range(3)), tuple(max(b[i] for b in bots) for i in range(3)))

q = PriorityQueue()
q.put((-len(bots), 0, bigbox))

while not q.empty():
    reachable, dist, box = q.get()
    if all(v2 == v1+1 for v1, v2 in zip(*box)):
        print(dist)
        break

    for new_box in split(box):
        new_reachable = sum(dist_from_box(new_box, b[:3]) <= b[3] for b in bots)
        new_dist = dist_from_box(new_box, (0, 0, 0))
        q.put((-new_reachable, new_dist, new_box))
