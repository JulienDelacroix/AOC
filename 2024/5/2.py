import sys
from collections import defaultdict
import functools

blocks = list(sys.stdin.read().split("\n\n"))

all_after = defaultdict(set)
for line in blocks[0].splitlines():
    before, after = tuple(map(int, line.split("|")))
    all_after[before].add(after)

def compare(p1, p2):
    return -1 if p2 in all_after[p1] else 1

res = 0
for line in blocks[1].splitlines():
    update = list(map(int, line.split(",")))
    if any(set(update[:i]) & all_after[update[i]] for i in range(len(update))):
        update.sort(key=functools.cmp_to_key(compare))
        res += update[len(update)//2]        
print(res)
