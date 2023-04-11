import sys
import functools

circuit = {}

@functools.lru_cache(None)
def get_signal(wire):
    if wire not in circuit: return int(wire)

    exp = circuit[wire]
    if len(exp) == 1: 
        return get_signal(exp[0])
    if len(exp) == 2:
        action, right = exp
        assert(action == "NOT")
        return ~get_signal(right)
    if len(exp) == 3:
        left, action, right = exp
        v1 = get_signal(left)
        v2 = get_signal(right)

        if action == "AND": return v1 & v2
        if action == "OR": return v1 | v2
        if action == "LSHIFT": return v1 << v2
        if action == "RSHIFT": return v1 >> v2

for line in sys.stdin.read().splitlines():
    exp, wire = line.split(" -> ")
    circuit.update({wire: exp.split()})

print(get_signal("a"))
