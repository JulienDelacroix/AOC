import sys
import re
from queue import Queue

def movable(floor):
    for i1 in floor:
        for i2 in floor:
            if i1 != i2: yield frozenset({i1, i2})
        yield frozenset({ i1 })

def valid(items):
    generators = set(i[0] for i in items if i[1] == 'g')
    microchips = set(i[0] for i in items if i[1] == 'm')
    return len(generators) == 0 or all(c in generators for c in microchips)

def key(state):
    generators = {}
    microchips = {}
    floors, elevator = state
    for f, items in enumerate(floors):
        for i in items:
            (generators if i[1] == 'g' else microchips).update({i[0] : f})
    return (tuple(sorted((generators[e], microchips[e]) for e in generators.keys())), elevator)


floors = [ set() for _ in range(4) ]
for f, line in enumerate(sys.stdin.read().splitlines()):
    for item in re.findall("a ([\w-]+ \w+)", line):
        element, type = item.split()
        floors[f].add((element[0:2], type[0]))
floors[0].update([("el", 'g'), ("el", 'm'), ("di", 'g'), ("di", 'm')])

state = (tuple(map(frozenset, floors)), 0)
visited = set()
q = Queue()
q.put((0, state))

while not q.empty():
    cost, state = q.get()

    floors, elevator = state
    f0, f1, f2, _ = floors
    if len(f0) == len(f1) == len(f2) == 0:
        print(cost)
        break

    for move in [d for d in (-1, +1) if 0 <= (elevator + d) <= 3]:
        destination = elevator + move
        for items in movable(floors[elevator]):
            next_floors = list(floors)
            next_floors[elevator] = floors[elevator] - items
            next_floors[elevator + move] = floors[elevator + move] | items
            if not valid(next_floors[elevator]) or not valid(next_floors[elevator + move]):
                continue

            next_state = (tuple(next_floors), elevator + move)
            next_cost = cost + 1
            next_key = key(next_state)
            if next_key not in visited:
                visited.add(next_key)
                q.put((next_cost, next_state))
