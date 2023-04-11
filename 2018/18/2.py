import sys

def n8(pos):
    x, y = pos
    for next_x, next_y in [(x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
        yield (next_x, next_y)

openyards, trees, lumberyards = set(), set(), set()
grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        match c:
            case '.': openyards.add((x, y))
            case '|': trees.add((x, y))
            case '#': lumberyards.add((x, y))


step = 0
remaining = 1000000000
visited = {}
while remaining:
    new_openyards, new_trees, new_lumberyards = set(), set(), set()

    for o in openyards:
        if sum(acre in trees for acre in n8(o)) >= 3:
            new_trees.add(o)
        else:
           new_openyards.add(o)

    for t in trees:
        if sum(acre in lumberyards for acre in n8(t)) >= 3:
            new_lumberyards.add(t)
        else:
           new_trees.add(t)

    for l in lumberyards:
        if any(acre in lumberyards for acre in n8(l)) and any(acre in trees for acre in n8(l)):
            new_lumberyards.add(l)
        else:
           new_openyards.add(l)

    openyards, trees, lumberyards = new_openyards, new_trees, new_lumberyards

    step += 1
    remaining -= 1
    key = (frozenset(openyards), frozenset(trees), frozenset(lumberyards))
    if key not in visited:
        visited.update({key : step})
    else:
        cycle_len = step - visited[key]
        remaining = remaining % cycle_len

print(len(trees) * len(lumberyards))
