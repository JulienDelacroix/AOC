import sys
import re

def splitInterval(interval, mapping, offset):
    intersect = max(interval[0], mapping[0]), min(interval[1], mapping[1])
    if intersect[0] >= intersect[1]:
        return [], [interval]
    
    unmapped = []
    if interval[0] < mapping[0] < interval[1]:
        unmapped.append((interval[0], mapping[0]))

    if interval[0] < mapping[1] < interval[1]:
        unmapped.append((mapping[1], interval[1]))

    return [(intersect[0] + offset, intersect[1] + offset)], unmapped

blocks = list(sys.stdin.read().split("\n\n"))
items = list(map(int, re.findall(r"(\d+)", blocks[0].splitlines()[0])))
intervals = set((items[i], items[i] + items[i+1]) for i in range (0, len(items), 2))

for block in blocks:
    next_intervals = set()
    for line in block.splitlines()[1:]:
        dest_start, source_start, range_len = map(int, line.split())
        source_range = (source_start, source_start + range_len)
        for r in list(intervals):
            mapped, unmapped = splitInterval(r, source_range, dest_start - source_start) 
            intervals.remove(r)
            intervals |= set(unmapped)
            next_intervals |= set(mapped)

    intervals |= next_intervals

print(min(i[0] for i in intervals))
