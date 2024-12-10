import sys
import re
from queue import PriorityQueue

def n4(pos):
    x, y = pos
    for ox, oy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        if (0 <= (x + ox) <= xmax) and (0 <= (y + oy) <= ymax):
            yield (x + ox, y + oy)

def dist(pos1, pos2):
    return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])


input()
input()
nodes = {}
xmax, ymax = 0, 0
for line in sys.stdin.read().splitlines():
    x, y, s, u = map(int, re.findall(r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T.*", line)[0])
    nodes.update({(x, y) : (s, u)})
    xmax, ymax = max(xmax, x), max(ymax, y)
    if u == 0: hole = (x, y)

# A* search
def h(state):
    hole, data = state
    return dist(data, (0,0)) + dist(hole, data)

q = PriorityQueue()
state = (hole, (xmax, 0))
q.put((h(state), state))
tracker = { state : 0 }

while not q.empty():
    _, state = q.get()
    hole, data = state
    if data == (0, 0):
        print(tracker[state])
        break
    
    new_cost = tracker[state] + 1
    for next_hole in n4(hole):
        if nodes[next_hole][1] > nodes[hole][0]: continue

        next_state = (next_hole, hole if next_hole == data else data)
        if next_state not in tracker or tracker[next_state] > new_cost:
            tracker.update({next_state : new_cost})
            new_priority = new_cost + h(next_state)
            q.put((new_priority, next_state))
