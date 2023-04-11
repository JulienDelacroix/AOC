import sys
import queue
import numpy as np

def arround(pos):
    y, x = pos
    if y+1 < H: yield (y + 1, x)
    if y > 0: yield (y - 1, x)
    if x+1 < W: yield (y, x + 1)
    if x > 0: yield (y, x - 1)

def heuristic(source, dest) -> float:
    (y1, x1) = source
    (y2, x2) = dest
    return abs(x1 - x2) + abs(y1 - y2)

grid = np.array([[int(c) for c in l] for l in sys.stdin.read().splitlines()])
grid = np.concatenate([(grid+x-1)%9 + 1 for x in range(0, 5)])
grid = np.concatenate([(grid+x-1)%9 + 1 for x in range(0, 5)], axis=1)
H, W = grid.shape

start = (0, 0)
goal = (H-1, W-1)

openset = queue.PriorityQueue()
visited = set()
costs = np.full(grid.shape, 1000000)
costs[start] = 0

openset.put((0 + heuristic(start, goal), start))
while not openset.empty():
    _p, pos = openset.get()
    if pos in visited: continue
    if pos == goal: break
    visited.add(pos)
    
    for next_pos in arround(pos):
        weight = grid[next_pos]
        new_cost = costs[pos] + weight
        if new_cost < costs[next_pos]:
            costs[next_pos] = new_cost
            openset.put((new_cost + heuristic(next_pos, goal), next_pos))

print(costs[goal])
print(len(visited), H*W)
