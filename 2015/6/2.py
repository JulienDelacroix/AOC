import sys
import re
from collections import Counter

tracker = Counter()
for line in sys.stdin.read().splitlines():
    action, x1s, y1s, x2s, y2s = re.findall("(.*) (\d+),(\d+) through (\d+),(\d+)", line)[0]
    x1, y1, x2, y2 = map(int, (x1s, y1s, x2s, y2s))
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            pos = (x, y)
            if action == "turn on": tracker[pos] += 1
            elif action == "turn off": tracker[pos] = max(0, tracker[pos]-1)
            elif action == "toggle": tracker[pos] += 2

print(sum(tracker.values()))
