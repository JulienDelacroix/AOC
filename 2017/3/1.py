offsets = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def fill(i, x, y, o, n):
    for _ in range(n):
        x, y = x + offsets[o][0], y + offsets[o][1]
        i += 1
        if i == target:
            print(abs(x) + abs(y))
            exit(0)
    return i, x, y

target = int(input())
o = x = y = 0
i = n = 1
while True:
    i, x, y = fill(i, x, y, o, n)
    o = (o + 1) % 4

    i, x, y = fill(i, x, y, o, n)
    o = (o + 1) % 4

    n += 1
