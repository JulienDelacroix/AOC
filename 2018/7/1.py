import sys
import re
import string

deps = { n : [] for n in string.ascii_uppercase }
remaining = set()
for line in sys.stdin.read().splitlines():
    before, after = re.findall(r"Step (\w+) must be finished before step (\w+) can begin", line)[0]
    deps[after].append(before)
    remaining.add(before)
    remaining.add(after)

while remaining:
    node = min(r for r in remaining if all(d not in remaining for d in deps[r]))
    print(node, end="")
    remaining.discard(node)
print()
