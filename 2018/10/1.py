import sys
import re

lights = []
speeds = []

for line in sys.stdin.read().splitlines():
    x, y, dx, dy = map(int, re.findall(r"(-?\d+)", line))
    lights.append([x, y])
    speeds.append([dx, dy])

for t in range(200000):
    for i in range(len(lights)):
        lights[i][0] += speeds[i][0]
        lights[i][1] += speeds[i][1]
    
    xmin = min(l[0] for l in lights)
    xmax = max(l[0] for l in lights)
    ymin = min(l[1] for l in lights)
    ymax = max(l[1] for l in lights)

    if(xmax-xmin < 200 and ymax - ymin <= 10):
        light_set = set(map(tuple, lights))
        for y in range(ymin, ymax+1):
            for x  in range(xmin, xmax+1):
                print('#' if (x, y) in light_set else '.', end="")
            print()
        print()
        break

