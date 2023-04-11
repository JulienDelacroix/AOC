import sys
from collections import defaultdict
from queue import Queue
import math

modules = {}
states = defaultdict(int)
inputs = defaultdict(dict)

def dot():
    print("digraph D {")
    print("edge [dir=\"back\"];")

    for name, (type, _)  in modules.items():
        shape = {'F' : "box", 'C': "diamond", 'B' : "circle"}
        print("%s [shape=%s]" % (name, shape[type]))

    for source, (_, destinations)  in modules.items():
        for d in destinations:
            print(d, "->", source)
    print("}")

    
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
        if d == "rx":
            conj_before_rx = name

required_input_cyles = { i : 0 for i in inputs[conj_before_rx] }

pushed = 0
while not all(required_input_cyles.values()):
    q = Queue()
    q.put(("button", "broadcaster", 0))
    pushed +=1
    while not q.empty():
        source, name, pulse = q.get()
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

        if name in required_input_cyles and new_pulse == 1:
            required_input_cyles[name] = pushed

print(math.lcm(*required_input_cyles.values()))
