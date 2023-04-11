import math

SERIAL = 8772

def power(x, y):
    rack_id = x + 10
    power = rack_id * y
    power += SERIAL
    power *= rack_id
    power_str = str(power)
    return (int(power_str[-3]) if len(power_str) >= 3 else 0) -5

grid = [ [power(x, y) for x in range(300)] for y in range(300)]

best = -math.inf
res = None, None
for y in range(0, 300-3):
    for x in range(0, 300-3):
        p = sum(sum(row[x:x+3]) for row in grid[y:y+3])
        if p > best:
            best = p
            res = [x, y]

print(",".join(map(str, res)))
