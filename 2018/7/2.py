import sys
import re
import string

deps = { n : [] for n in string.ascii_uppercase }
remaining = {}
for line in sys.stdin.read().splitlines():
    before, after = re.findall(r"Step (\w+) must be finished before step (\w+) can begin", line)[0]
    deps[after].append(before)
    remaining.update({before : None})
    remaining.update({after : None})

workers = 5
t = 0
while remaining:
    for node, exp in list(sorted(remaining.items())):
        if exp == t:
            del remaining[node]
            workers += 1

    ready = [r for r, exp in remaining.items() if exp is None and all(d not in remaining for d in deps[r])]
    for node in sorted(ready):
        if workers:
            remaining[node] = t + string.ascii_uppercase.index(node) + 61
            workers -=1
    t += 1

print(t-1)
