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
max_x = max(pos[0] for pos in grid.keys())
max_y = max(pos[1] for pos in grid.keys())



# patch input
for dx in (-1, 0, 1):
    for dy in (-1, 0, 1):
        x, y = start_pos[0] + dx, start_pos[1] + dy
        if (x, y) in grid:
            grid.update({(x, y) : '.' if abs(dx)+abs(dy) == 2 else '#'})


for y in range(max_y+1):
    for x in range(max_x+1):
        print(grid[(x, y)], end="")
    print()

q = PriorityQueue()
start_state = (tuple(s for s in n4(start_pos)), frozenset(all_keys.keys()))
q.put((0, 0, start_state))
visited = {start_state : 0 }

while not q.empty():
    prio, t, state = q.get()
    print("GET", prio, t, state)
    
    pos_list, missing_keys = state
    if len(missing_keys) == 0:
        print(t)
        break

    for i, pos in enumerate(pos_list):
        for new_pos in n4(pos):
            if new_pos not in grid: continue
            if grid[new_pos] == '#': continue
            if grid[new_pos] in string.ascii_uppercase and grid[new_pos].lower() in missing_keys: continue

            new_missing_keys = (missing_keys - frozenset([grid[new_pos]])) if grid[new_pos] in string.ascii_lowercase else missing_keys
            new_pos_list = tuple(new_pos if n == i else pos_list[n] for n in range(4))
            new_state = (new_pos_list, new_missing_keys)
            new_t = t + 1
            new_prio = new_t
            # if len(new_missing_keys):
            #     new_prio += len(new_missing_keys) * min( abs(all_keys[k][0] - new_pos[0]) + abs(all_keys[k][1] - new_pos[1]) for k in new_missing_keys)

            print("PUT", new_prio, new_t, new_state)
            if new_state not in visited or new_t < visited[new_state]:
                visited.update({ new_state : new_t})
                q.put((new_prio, new_t, new_state))
            