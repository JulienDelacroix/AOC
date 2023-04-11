import sys
import math
import itertools

# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
def intersect(pos1, speed1, pos2, speed2):
    x1, x2 = pos1[0], pos1[0] + speed1[0]
    y1, y2 = pos1[1], pos1[1] + speed1[1]
    x3, x4 = pos2[0], pos2[0] + speed2[0]
    y3, y4 = pos2[1], pos2[1] + speed2[1]

    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator == 0: 
        return False

    # compute intersection
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator
    
    # check intersection happens in the "future"
    if math.copysign(1, x2 - x1) != math.copysign(1, px - x1): return False
    if math.copysign(1, x4 - x3) != math.copysign(1, px - x3): return False

    # check against test window
    return (200000000000000 <= px <= 400000000000000 and 200000000000000 <= py <= 400000000000000)

hailstones = []
for line in sys.stdin.read().splitlines():
    s1, s2 = line.split("@")
    pos = tuple(map(int, s1.split(",")))
    speed = tuple(map(int, s2.split(",")))

    hailstones.append((pos, speed))

print(sum(intersect(*h1, *h2) for h1, h2 in itertools.combinations(hailstones, 2)))
