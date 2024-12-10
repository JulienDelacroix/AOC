import sys
import itertools
import collections

antennas = collections.defaultdict(list)

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})
        if c != '.':
            antennas[c].append((x, y))

antinodes = set()
for pos_list in antennas.values():
    for pos1, pos2 in itertools.product(pos_list, repeat=2):
        if pos1 != pos2:
            delta = tuple(v2 -v1 for v1, v2 in zip(pos1, pos2))
            npos = tuple((v + dv) for v, dv in zip(pos1, delta))
            if npos in grid:
                antinodes.add(npos)

print(len(antinodes))
