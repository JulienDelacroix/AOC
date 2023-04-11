import sys
from collections import defaultdict
from queue import Queue

def n4(pos): 
    x, y = pos
    yield (x, y-1)
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y+1)

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})

dist = defaultdict(lambda: 10000)
start = next(k for k, v in grid.items() if v == 'S')
stop = next(k for k, v in grid.items() if v == 'E')

grid[start] = 'a'
grid[stop] = 'z'

queue = Queue()
dist[start] = 0
queue.put(start)

while not queue.empty():
    pos = queue.get()
    for next_pos in n4(pos):
        if next_pos not in grid: continue
        if ord(grid[next_pos]) <= ord(grid[pos])+1 and dist[next_pos]>dist[pos]+1:
            dist[next_pos] = dist[pos]+1
            queue.put((next_pos))

print(dist[stop])
