import sys
from collections import defaultdict

blocks = list(sys.stdin.read().split("\n\n"))

all_after = defaultdict(set)
for line in blocks[0].splitlines():
    before, after = tuple(map(int, line.split("|")))
    all_after[before].add(after)

res = 0
for line in blocks[1].splitlines():
    update = list(map(int, line.split(",")))
    if not any(set(update[:i]) & all_after[update[i]] for i in range(len(update))):
        res += update[len(update)//2]
print(res)
