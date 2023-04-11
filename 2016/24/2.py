import sys
from queue import Queue

def n4(pos):
    x, y = pos
    for ox, oy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        yield (x + ox, y + oy)

walls = set()
targets = set()
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        pos = (int(x), int(y))
        if c == '#':
            walls.add(pos)
        elif c != '.':
            if c == '0': 
                start = pos
            targets.add(pos)

distances = {}
for t in targets:
    visited = set()
    q = Queue()
    q.put((t, 0))
    visited.add(t)
    while not q.empty():
        pos, d = q.get()
        if pos in targets:
            distances.update({(t, pos) : d})
        for npos in n4(pos):
            if npos not in walls and npos not in visited:
                q.put((npos, d+1))
                visited.add(npos)

best = 100000
def dfs(pos, cost, targets):
    global best

    if len(targets) == 0:
        best = min(best, cost + distances[(pos, start)])
        return
    
    if cost < best:
        for t in targets:
            dfs(t, cost + distances[(pos, t)], targets - {t})

dfs(start, 0, targets - {start})
print(best)