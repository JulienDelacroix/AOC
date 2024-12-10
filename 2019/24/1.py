import sys

def n4(pos): 
    x, y = pos
    if y != 0: yield (x, y-1)
    if x != 0: yield (x-1, y)
    if x != 4: yield (x+1, y)
    if y != 4: yield (x, y+1)

bugs = set()
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c == '#':
            bugs.add((x, y))

visited = set()
while True:
    biodiversity = sum(pow(2, y * 5 + x) for x, y in bugs)
    if biodiversity in visited:
        print(biodiversity)
        break
    visited.add(biodiversity)
    
    next_bugs = set()
    for pos in bugs:
        if sum(npos in bugs for npos in n4(pos)) == 1:
            next_bugs.add(pos)
        
        for potential in n4(pos):
            if potential not in bugs:
                if 1 <= sum(npos in bugs for npos in n4(potential)) <= 2:
                    next_bugs.add(potential)
    bugs = next_bugs
