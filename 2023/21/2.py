import sys
import numpy

def n4(pos):
    x, y = pos
    for ox, oy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        yield (x + ox, y + oy)

reachable = set()
grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c == 'S':
            reachable.add((x, y))
            c = '.'
        grid.update({(x, y) : c})

xmax = max(p[0] for p in grid.keys()) + 1
ymax = max(p[1] for p in grid.keys()) + 1

STEPS = 26501365

# OBSERVATIONS:
# From the center of a grid:
#  1) the center of the next left/right grid is reached in *exactly* xmax steps
#  2) all pos in a grid have been reached after *exactly* xmax steps
#    (from this point, the grid state alternates between selecting all "even" pos and all "odd" pos)
#
# CONCLUSION: 
# Every xmax steps:
#  - the "border" is a combination of repeating patterns, and it is growing linearly
#  - the "inner" has as fixed pattern with all "odd" or all "even" pos selected, and it is growing quadratically
#  => #reachable after (u * xmax + R) steps = A(R)u^2 + B(R)u + C(R)

# compute samples for u in {0, 1, 2} and R = STEPS % xmax
R = STEPS % xmax
samples = []
for step in range(STEPS):
    next_reachable = set()
    for pos in reachable:
        for npos in n4(pos):
            nx, ny = npos
            if grid[(nx % xmax, ny % ymax)] == '.':
                next_reachable.add(npos)

    if step == (len(samples) * xmax + R):
        samples.append(len(reachable))
        if(len(samples) == 3): break

    reachable = next_reachable

# fit samples with degree 2 polynomial to find A(R), B(R), and C(R)
polynomial = map(int, reversed(numpy.polyfit((0, 1, 2), samples, 2)))

# compute reachable after (u * xmax + R) = STEPS steps
u = STEPS // xmax
print(sum(coeff * u**n for n, coeff in enumerate(polynomial)))
