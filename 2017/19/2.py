import sys

def nextPos(p, dir):
    x, y = p
    return ((x, y-1), (x+1, y), (x, y+1), (x-1, y))[dir]

def nextDir(p, dir):
    c = grid[p]
    if (c == '+'): 
        for d in ((1, 3), (0, 2), (1, 3), (0, 2))[dir]:
            pos = nextPos(p, d)
            while pos in grid:
                if grid[pos] != "|-|-"[dir]:
                    return d
                pos = nextPos(pos, d)
        return None
    else:
        return dir            

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c != ' ':
            grid.update({ (x,y) : c })
        if y == 0 and c == '|':
            pos = (x, y)

dir = 2
res = 0
while pos in grid:
    dir = nextDir(pos, dir)
    pos = nextPos(pos, dir)
    res += 1

print(res)
