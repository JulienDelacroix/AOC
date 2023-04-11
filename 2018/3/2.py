import sys
import re

claims = {}
overlap = set()
for line in sys.stdin.read().splitlines():
    id, xstart, ystart, xsize, ysize = map(int, re.findall("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)[0])
    for x in range(xstart, xstart + xsize):
        for y in range(ystart, ystart + ysize):
            if (x, y) in claims:
                overlap.add(claims[(x, y)])
                overlap.add(id)
            claims.update({(x, y) : id})

print(*(set(claims.values()) - overlap))
