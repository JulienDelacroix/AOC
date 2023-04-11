def dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)) // 2

res = 0
x = y = z = 0
for d in input().split(","):
    if d == "n": 
        y += 1
        z -= 1
    elif d == "ne":
        x += 1
        z -= 1
    elif d == "se":
        x += 1
        y -= 1
    elif d == "s":
        y -= 1
        z += 1
    elif d == "sw":
        x -= 1
        z += 1
    elif d == "nw":
        x -= 1
        y += 1
    res = max(res, dist((0, 0, 0), (x, y, z)))
print(res)
