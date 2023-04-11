import sys
import re

tracker = set()

for line in sys.stdin.read().splitlines():
    action, coord = line.split()
    x1, x2, y1, y2, z1, z2 = map(int, re.findall("x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)", coord)[0])
    if any(v < -50 for v in (x1, y1, z1)): continue
    if any(v > 50 for v in (x2, y2, z2)): continue    

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                if action == "on":
                    tracker.add((x, y, z))
                elif (x, y, z) in tracker:
                    tracker.remove((x, y, z))

print(len(tracker))
