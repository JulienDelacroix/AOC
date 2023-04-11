import sys
import re

def distance(speed, duration, rest, time):
    div, mod = divmod(time, duration+rest)
    return (div*duration + min(mod, duration)) * speed

reindeers = []
for line in sys.stdin.read().splitlines():
    speed, duration, rest = map(int, re.findall("\d+", line))
    reindeers.append([distance(speed, duration, rest, time) for time in range(2504)])

first = list(map(max, zip(*reindeers)))
print(max(sum(reindeers[r][t] == first[t] for t in range(1, 2504)) for r in range(len(reindeers))))
