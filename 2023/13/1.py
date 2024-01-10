import sys

def symetricPairs(axis, maxval):
    for d in range(maxval):
        if (axis-d) >= 0 and (axis+1+d) < maxval:
            yield (axis-d, axis+d+1)
    
res = 0
for pattern_lines in sys.stdin.read().split("\n\n"):
    pattern = pattern_lines.splitlines()
    x_max, y_max = len(pattern[0]), len(pattern)

    for x_axis in range(x_max-1):
        if all(pattern[y][x1] == pattern[y][x2] for x1, x2 in symetricPairs(x_axis, x_max) for y in range(y_max)):
            res += (x_axis + 1)

    for y_axis in range(y_max-1):
        if all(pattern[y1][x] == pattern[y2][x] for y1, y2 in symetricPairs(y_axis, y_max) for x in range(x_max)):
            res += (y_axis + 1) * 100

print(res)
