import sys

def n4(pos):
    x, y = pos
    for npos in [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]:
        if npos in grid and grid[npos] == grid[pos] + 1:
            yield npos

def solve(pos, visited):
    if pos in visited:
        return 0
    visited.add(pos)
    
    return 1 if grid[pos] == 9 else sum(solve(npos, visited) for npos in n4(pos))
    

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c != '.':
            grid.update({(x, y) : (int(c) if c != '.' else -1)})

print(sum(solve(pos, set()) for pos, val in grid.items() if val == 0))
