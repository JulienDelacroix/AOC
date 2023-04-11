import sys
from collections import defaultdict
from queue import Queue

modules = {}
states = defaultdict(int)
inputs = defaultdict(dict)

for line in sys.stdin.read().splitlines():
    module, destinations_str = line.split(" -> ")
    destinations = tuple(destinations_str.split(", "))
    if module[0] == '%':
        type, name = 'F', module[1:]
    elif module[0] == '&':
        type, name = 'C', module[1:]
    else:
        type, name = 'B', module
    modules.update({(name, (type, destinations))})
    for d in destinations:
        inputs[d][name] = 0

counters = [0, 0]
for pushed in range(1000):
    q = Queue()
    q.put(("button", "broadcaster", 0))
    while not q.empty():
        source, name, pulse = q.get()
        counters[pulse] += 1
        if name not in modules:
            continue

        type, destinations = modules[name]
        if type == 'F':
            if pulse == 0:
                states[name] = 1 - states[name]
                new_pulse = states[name]
            else:
                continue
        elif type == 'C':
            inputs[name][source] = pulse
            new_pulse = 1 - all(i == 1 for i in inputs[name].values())
        else:
            new_pulse = pulse

        for d in destinations:
            q.put((name, d, new_pulse))

print(counters[0] * counters[1])
