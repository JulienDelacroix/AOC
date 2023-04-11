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
cumulativeSums = [[0] * 300]

for row in grid:
    cumulativeSums.append([cumulated + v for cumulated, v in zip(cumulativeSums[-1], row)])

best = -math.inf
res = None, None, None
for top in range(0, 300):
    for bottom in range(top+1, 300+1):
        size = bottom - top
        values = [b - t for b, t in zip(cumulativeSums[bottom], cumulativeSums[top])]

        for left in range(300 - size):
            p = sum(values[left:left+size])
            if p > best:
                best = p
                res = left, top, size

print(",".join(map(str, res)))
