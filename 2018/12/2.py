import sys

init = input().split(": ")[1]
input()
plants = set(i for i, v in enumerate(init) if v == '#')

rules = {}
for rule in sys.stdin.read().splitlines():
    pattern, result = rule.split(" => ")
    rules.update({tuple(c == '#' for c in pattern) : result == '#'})

history = []
for step in range(1000):
    new_plants = set()
    updatable = set(v for p in plants for v in range(p-4, p+5))
    for pot in updatable:
        pattern = tuple(p in plants for p in range(pot-2, pot+3))
        if pattern in rules and rules[pattern]:
            new_plants.add(pot)
    delta = sum(new_plants) - sum(plants)
    if len(history) > 10 and all(d == delta for d in history[-10:]):
        break
    plants = new_plants
    history.append(delta)

print(sum(plants) + (50000000000-step) * delta)
