import sys
from queue import Queue

def n8(pos):
    x, y = pos
    for next_x, next_y in [(x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
        if 0 <= next_x < 10 and 0 <= next_y < 10:
            yield next_x, next_y

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({ (x,y) : int(c) })

res = 0
for _ in range(100):
    flashed = set()
    q = Queue()
    for pos in grid.keys():
        grid[pos] += 1
        if grid[pos] > 9:
            q.put(pos)
    flashed.update(q.queue)

    while not q.empty():
        flashed_pos = q.get()
        for next_pos in n8(flashed_pos):
            grid[next_pos] += 1
            if grid[next_pos] > 9 and next_pos not in flashed:
                flashed.add(next_pos)
                q.put(next_pos)

    res += len(flashed)
    for pos in flashed:
        grid[pos] = 0

print(res)
