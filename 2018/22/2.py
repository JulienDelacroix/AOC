import re
import functools
from queue import PriorityQueue

@functools.lru_cache(None)
def erosion(x, y):
    if x == target_x and y == target_y: return  depth % 20183 
    if y == 0: return ((x * 16807) + depth) % 20183
    if x == 0: return ((y * 48271) + depth) % 20183
    return ((erosion(x-1, y) * erosion(x, y-1)) + depth ) % 20183

def n4(pos): 
    x, y = pos
    yield (x, y-1)
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y+1)

usable = [ ['C', 'T'], ['C', 'N'], ['T', 'N'] ]

depth = int(re.findall("(\d+)", input())[0])
target_x, target_y = tuple(map(int, re.findall("(\d+)", input())))

visited = {}
q = PriorityQueue()
q.put((0, 0, ((0, 0), "T")))
while not q.empty():
    prio, t, state = q.get()
    if state in visited and visited[state] <= t:
        continue
    visited[state] = t
    
    pos, gear = state
    x, y = pos
    if state == ((target_x, target_y), 'T'):
        print(t)
        break

    new_states = []
    for new_gear in usable[erosion(x, y) % 3]:
        if new_gear != gear:
            new_state = (pos, new_gear)
            new_t = t + 7
            new_prio = new_t + abs(target_x - x) + abs(target_y - y)
            q.put((new_prio, new_t, new_state))

    for new_pos in n4(pos):
        new_x, new_y = new_pos
        if new_x < 0 or new_y < 0 or gear not in usable[erosion(new_x, new_y) % 3]:
            continue

        new_state = (new_pos, gear)
        new_t = t + 1
        new_prio = new_t + abs(target_x - new_x) + abs(target_y - new_y)
        q.put((new_prio, new_t, new_state))