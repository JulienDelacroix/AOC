import sys
import re

blocks = list(sys.stdin.read().split("\n\n"))
items = set(map(int, re.findall("(\d+)", blocks[0].splitlines()[0])))

for block in blocks:
    next_items = set()
    for line in block.splitlines()[1:]:
        dest_start, source_start, range_len = map(int, line.split())
        for i in list(items):
            if source_start <= i < (source_start + range_len):
                next_items.add(dest_start + (i - source_start))
                items.remove(i)

    items |= next_items

print(min(items))
