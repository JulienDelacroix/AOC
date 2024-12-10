import sys
import re
from queue import Queue

values = {}
rules = {}

q = Queue()
for line in sys.stdin.read().splitlines():
    if line.startswith("value"):
        v, bot = re.findall(r"value (\d+) goes to (.*)", line)[0]
        if bot in values:
            values[bot].append(int(v))
            q.put(bot)
        else:
            values.update({ bot : [int(v)] })
    else:
        source, low, high = re.findall(r"(.*) gives low to (.*) and high to (.*)", line)[0]
        rules.update({ source : (low, high) })

while not q.empty():
    bot = q.get()
    vmin, vmax = sorted(values[bot])

    if bot in rules:
        dest1, dest2 = rules[bot]
        if dest1 in values:
            values[dest1].append(vmin)
            q.put(dest1)
        else:
            values.update({ dest1 : [vmin] })
        if dest2 in values:
            values[dest2].append(vmax)
            q.put(dest2)
        else:
            values.update({ dest2 : [vmax] })

print(values["output 0"][0] *values["output 1"][0] * values["output 2"][0])