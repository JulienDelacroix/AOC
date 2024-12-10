import sys
import re
from queue import Queue

clays = set()

for line in sys.stdin.read().splitlines():
    fixed_coord, fixed_val, range_begin, range_end = re.findall(r"(.)=(\d+), .=(\d+)\.\.(\d+)", line)[0]
    for r in range(int(range_begin), int(range_end)+1):
        clays.add((int(fixed_val), r) if fixed_coord=='x' else (r, int(fixed_val)))

xmin = min(v[0] for v in clays)
ymin = min(v[1] for v in clays)

xmax = max(v[0] for v in clays)
ymax = max(v[1] for v in clays)

settled = set()
reachable = set()

spring = (500, 0)
q = Queue ()
q.put(spring)

while not q.empty():
    x, y  = q.get()
    reachable.add((x, y))

    # fall down
    while (x, y+1) not in clays and (x, y+1) not in settled and y <= ymax+1:
        y += 1
        reachable.add((x, y))
    if y > ymax: continue
    
    falldown = False

    # flow on the right
    for x_right in range(x+1, xmax+2):
        right = (x_right, y)
        if right in clays:
            break
        if (x_right, y+1) not in clays and (x_right, y+1) not in settled:
            # fall down on the right
            falldown = True
            if right not in q.queue:
                q.put(right)
            break
        reachable.add(right)

    # flow on the left
    for x_left in range(x-1, xmin-2, -1):
        left = (x_left, y)
        if left in clays:
            break
        if (x_left, y+1) not in clays and (x_left, y+1) not in settled:
            # fall down on the left
            falldown = True
            if left not in q.queue:
                q.put(left)
            break
        reachable.add(left)

    # fill up
    if not falldown:
        settled.update((settled_x, y) for settled_x in range(x_left+1, x_right))
        if (x, y-1) not in q.queue:
            q.put((x, y-1))

print(sum(1 for p in settled if ymin <= p[1] <= ymax))
