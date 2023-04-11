import sys
import re

def intersects(c1, c2):
    return all(c1[start] < c2[end] and c1[end] > c2[start] for (start, end) in [(0, 1), (2, 3), (4, 5)])

def contains(outside, inside):
    return all(outside[start] <= inside[start] and outside[end] >= inside[end] for (start, end) in [(0, 1), (2, 3), (4, 5)])

def volume(box):
    return (box[1] - box[0]) * (box[3] - box[2]) * (box[5] - box[4])

def dfs(box, cubes):
    intersection = [c for c in cubes if intersects(box, c)]
    for c in intersection:
        if not contains(c, box):
            if box[0] < c[0]:
                return dfs((box[0], c[0], box[2], box[3], box[4], box[5]), intersection) + dfs((c[0], box[1], box[2], box[3], box[4], box[5]), intersection)

            if box[1] > c[1]:
                return dfs((box[0], c[1], box[2], box[3], box[4], box[5]), intersection) + dfs((c[1], box[1], box[2], box[3], box[4], box[5]), intersection)

            if box[2] < c[2]:
                return dfs((box[0], box[1], box[2], c[2], box[4], box[5]), intersection) + dfs((box[0], box[1], c[2], box[3], box[4], box[5]), intersection)

            if box[3] > c[3]:
                return dfs((box[0], box[1], box[2], c[3], box[4], box[5]), intersection) + dfs((box[0], box[1], c[3], box[3], box[4], box[5]), intersection)

            if box[4] < c[4]:
                return dfs((box[0], box[1], box[2], box[3], box[4], c[4]), intersection) + dfs((box[0], box[1], box[2], box[3], c[4], box[5]), intersection)

            if box[5] > c[5]:
                return dfs((box[0], box[1], box[2], box[3], box[4], c[5]), intersection) + dfs((box[0], box[1], box[2], box[3], c[5], box[5]), intersection)

            assert(False)
        else:
            return volume(box) if c[6] else 0

    return  0

cubes = []
for line in sys.stdin.read().splitlines():
    action, coord = line.split()
    x1, x2, y1, y2, z1, z2 = map(int, re.findall("x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)", coord)[0])
    cubes.append((x1, x2+1, y1, y2+1, z1, z2+1, action == "on"))

print(
    dfs(
        (
            min(c[0] for c in cubes), max(c[1] for c in cubes),
            min(c[2] for c in cubes), max(c[3] for c in cubes),
            min(c[4] for c in cubes), max(c[5] for c in cubes)
        ), reversed(cubes)
    )
)
