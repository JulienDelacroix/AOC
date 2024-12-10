import sys
import re

scores = []
for line in sys.stdin.read().splitlines():
    speed, duration, rest = map(int, re.findall(r"\d+", line))
    div, mod = divmod(2503, duration+rest)
    scores.append((div*duration + min(mod, duration)) * speed)
print(max(scores))
