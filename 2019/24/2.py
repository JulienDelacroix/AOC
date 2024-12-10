import sys

def allNext(pos): 
    x, y, d = pos
    # UP
    if y == 0:
        yield (2, 1, d-1) # outer
    elif (x, y) == (2, 3):
        for i in range(5):
            yield (i, 4, d + 1) # inner
    else:
        yield (x, y-1, d) # same level
    
    # RIGHT
    if x == 4:
        yield (3, 2, d-1) # outer
    elif (x, y) == (1, 2):
        for i in range(5):
            yield (0, i, d + 1) # inner
    else:
        yield (x+1, y, d) # same level

    # BOTTOM
    if y == 4:
        yield (2, 3, d-1) # outer
    elif (x, y) == (2, 1):
        for i in range(5): # inner
            yield (i, 0, d + 1)
    else:
        yield (x, y+1 , d) # same

    # LEFT
    if x == 0:
        yield (1, 2, d-1) # outer
    elif (x, y) == (3, 2):
        for i in range(5):
            yield (4, i, d + 1) # inner level
    else:
        yield (x-1, y, d) # same level
    

bugs = set()
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c == '#':
            bugs.add((x, y, 0))

for r in range(200):
    next_bugs = set()
    for pos in bugs:
        if sum(npos in bugs for npos in allNext(pos)) == 1:
            next_bugs.add(pos)
        
        for potential in allNext(pos):
            if potential not in bugs:
                if 1 <= sum(npos in bugs for npos in allNext(potential)) <= 2:
                    next_bugs.add(potential)
    bugs = next_bugs
    
print(len(bugs))
