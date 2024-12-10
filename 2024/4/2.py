import sys

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})

def diag(pos):
    x, y = pos
    yield ((x-1, y-1), (x+1, y+1))
    yield ((x-1, y+1), (x+1, y-1))

def ms(p1, p2):
    return p1 in grid and p2 in grid and tuple(sorted([grid[p1], grid[p2]])) == ('M', 'S')
    
def xmas(pos):
    return grid[pos] == 'A' and sum(ms(p1, p2) for p1, p2 in diag(pos)) == 2

print(sum(xmas(pos) for pos in grid.keys()))
