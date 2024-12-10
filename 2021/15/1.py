import sys
import queue
import numpy as np

def arround(pos):
    y, x = pos
    if y+1 < H: yield (y + 1, x)
    if y > 0: yield (y - 1, x)
    if x+1 < W: yield (y, x + 1)
    if x > 0: yield (y, x - 1)

grid = np.array([[int(c) for c in l] for l in sys.stdin.read().splitlines()])
H, W = grid.shape

start = (0, 0)
goal = (H-1, W-1)

q = queue.PriorityQueue()
visited = set()
costs = np.full(grid.shape, 1000000)
costs[start] = 0

# A* search
def h(source, dest) -> float:
    (y1, x1) = source
    (y2, x2) = dest
    return abs(x1 - x2) + abs(y1 - y2)

q.put((0 + h(start, goal), start))
while not q.empty():
    _, pos = q.get()
    if pos in visited: continue
    if pos == goal: break
    visited.add(pos)
    
    for next_pos in arround(pos):
        weight = grid[next_pos]
        new_cost = costs[pos] + weight
        if new_cost < costs[next_pos]:
            costs[next_pos] = new_cost
            q.put((new_cost + h(next_pos, goal), next_pos))

print(costs[goal])
