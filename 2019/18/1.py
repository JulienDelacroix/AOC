import sys
import string
from queue import PriorityQueue

def n4(pos): 
    x, y = pos
    for p in ((x, y-1), (x-1, y), (x+1, y), (x, y+1)):
        yield p

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c == '@':
            start_pos = (x, y)
        grid.update({(x, y) : '.' if c == '@' else c})

all_keys = { k : pos for pos, k in grid.items() if k in string.ascii_lowercase }

q = PriorityQueue()
start_state = (start_pos, frozenset(all_keys.keys()))
q.put((0, 0, start_state))
visited = {start_state : 0 }

while not q.empty():
    prio, t, state = q.get()
    
    pos, missing_keys = state
    if len(missing_keys) == 0:
        print(t)
        break

    for new_pos in n4(pos):
        if new_pos not in grid: continue
        if grid[new_pos] == '#': continue
        if grid[new_pos] in string.ascii_uppercase and grid[new_pos].lower() in missing_keys: continue

        new_missing_keys = (missing_keys - frozenset([grid[new_pos]])) if grid[new_pos] in string.ascii_lowercase else missing_keys
        new_state = (new_pos, new_missing_keys)
        new_t = t + 1
        new_prio = new_t

        if new_state not in visited or new_t < visited[new_state]:
            visited.update({ new_state : new_t})
            q.put((new_prio, new_t, new_state))
