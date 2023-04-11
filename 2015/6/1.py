import sys
import re

on = set()
for line in sys.stdin.read().splitlines():
    action, x1s, y1s, x2s, y2s = re.findall("(.*) (\d+),(\d+) through (\d+),(\d+)", line)[0]
    x1, y1, x2, y2 = map(int, (x1s, y1s, x2s, y2s))
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if action == "turn on": on.add((x, y))
            if action == "turn off" and (x, y) in on: on.remove((x, y))
            elif action == "toggle":
                if (x, y) in on: on.remove((x, y))
                else: on.add((x, y))
print(len(on))
