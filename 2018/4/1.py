import sys
import re
from collections import Counter

logs = []
for line in sys.stdin.read().splitlines():
    year, month, day, hour, min, text = re.findall("\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.*)", line)[0]
    logs.append((tuple(map(int, (year, month, day, hour, min))), text))

stats = {}
for log in sorted(logs):
    minutes, text = log[0][-1], log[1]
    if text.startswith("Guard"):
        guard = int(re.findall("#(\d+)", text)[0])
        guard_stat = stats.setdefault(guard, [0, Counter()])
    elif text == "falls asleep":
        sleep_time = minutes
    else:
        guard_stat[0] += (minutes - sleep_time)
        for m in range(sleep_time, minutes):
          guard_stat[1][m] += 1

max_sleep, best_min, best_guard = max((stat[0], stat[1].most_common(1)[0][0], guard) for guard, stat in stats.items() if len(stat[1]))
print(best_min * best_guard)
