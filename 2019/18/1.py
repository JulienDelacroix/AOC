import sys
import string
from collections import defaultdict
from queue import Queue
from queue import PriorityQueue

grid = {}
targets = defaultdict(list)

def n4(pos): 
    x, y = pos
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)

def computeDist(source, dest_list):
    visited = set()
    q = Queue()
    q.put((source, 0))
    visited.add(source)
    while not q.empty():
        pos, dist = q.get()
        if pos != source and pos in dest_list:
            targets[source].append((pos, dist))
        else:
            for npos in n4(pos):
                if npos in grid and grid[npos] != '#' and npos not in visited:
                    visited.add(npos)
                    q.put((npos, dist+1))
                    
# read grid
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c == '@':
            start_pos = (x, y)
        grid.update({(x, y) : c})


# compute targets
all_keys = { val for val in grid.values() if val in string.ascii_lowercase }
all_targets = { pos for pos, val in grid.items() if val != '.' and val != '#' }
for source in all_targets:
    computeDist(source, all_targets)
    targets[source].sort(key = lambda v : v[1])


# A* search
def h(state):
    _, missing_keys = state
    return len(missing_keys)

q = PriorityQueue()
start_state = (start_pos, frozenset(all_keys))
q.put((h(start_state), 0, start_state))
costs = {start_state : 0 }

while not q.empty():
    _, t, state = q.get()

    pos, missing_keys = state
    if len(missing_keys) == 0:
        print(t)
        break

    for new_pos, dist in targets[pos]:
        if grid[new_pos] in string.ascii_uppercase and grid[new_pos].lower() in missing_keys:
            continue

        new_missing_keys = (missing_keys - frozenset([grid[new_pos]]))
        new_state = (new_pos, new_missing_keys)
        new_t = t + dist

        if new_state not in costs or new_t < costs[new_state]:
            costs.update({ new_state : new_t})
            q.put((new_t + h(new_state),  new_t, new_state))
