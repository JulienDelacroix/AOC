import sys

R, D, L, U = range(4)
next_direction = {
    '|' : (None, D, None, U),
    '-' : (R, None, L, None),
    '/' : (U, L, D, R),
    '\\' : (D, R, U, L),
}

def nextPos(p, dir):
    x, y = p
    return ((x+1, y), (x, y+1), (x-1, y), (x, y-1))[dir]

grid = {}
cars = []
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        pos = (x, y)
        if c in ">v<^":
            dir = ">v<^".index(c)
            cars.append([pos, dir, 0])
            grid.update({pos : "-|-|"[dir]})
        else:
            grid.update({pos : c})

allpos = set(c[0] for c in cars)
while len(cars) != 1:
    allpos = {c[0] : i for i, c in enumerate(cars)}
    removed = set()    
    for i in range(len(cars)):
        pos, dir, turns = cars[i]
        if i in removed: continue

        if grid[pos] == '+':
            ndir = (dir + 4 + (-1, 0, 1)[turns % 3]) % 4
            turns += 1
        else:            
            ndir = next_direction[grid[pos]][dir]
        npos = nextPos(pos, ndir)

        allpos.pop(pos)
        other = allpos.pop(npos, None)
        if other is not None:
            removed.add(i)
            removed.add(other)
        else:
            allpos.update({npos : i})
        cars[i] = (npos, ndir, turns)
    
    cars = [c for i, c in enumerate(cars) if i not in removed]
    cars.sort(key =lambda v : (v[0][1], v[0][0]))

print(",".join(map(str, cars[0][0])))
