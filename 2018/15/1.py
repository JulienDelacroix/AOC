import sys
from queue import Queue
from dataclasses import dataclass

@dataclass
class Unit:
    pos: tuple
    type: chr
    life: int = 200

grid = {}
units = []

def n4(pos): 
    x, y = pos
    yield (x, y-1)
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y+1)

def move(startPos, target): 
    q = Queue()
    visited = set()
    q.put((startPos, startPos))
    while not q.empty():
        pos, move = q.get()

        for npos in n4(pos):
            if npos not in grid: continue
            if grid[npos] == target:
                return move
            
            if grid[npos] == '.' and npos not in visited:
                visited.add(npos)
                q.put((npos, move if move != startPos else npos))
    return startPos


for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})
        if c == 'G' or c == 'E':
            units.append(Unit((x, y), c))

for fullrounds in range(1000):
    units = [u for u in units if u.life > 0]
    units.sort(key=lambda u: (u.pos[1], u.pos[0]))

    for u in units:
        if u.life < 0 : continue

        # check for remaining targets
        opptype = 'G' if u.type == 'E' else 'E'
        if not any(remaining.life > 0 for remaining in units if remaining.type == opptype):
            print(fullrounds * sum(remaining.life for remaining in units if remaining.life > 0))
            exit(0)
        
        # move
        grid[u.pos] = '.'
        u.pos = move(u.pos, opptype)
        grid[u.pos] = u.type

        # attack
        opplist = [opp for opp in units if opp.type == opptype and opp.life>0 and opp.pos in n4(u.pos)]
        opplist.sort(key = lambda opp: (opp.life, opp.pos[1], opp.pos[0]))

        if len(opplist):
            opp = opplist[0]
            opp.life -= 3
            if opp.life <= 0:
                grid[opp.pos] = '.'
