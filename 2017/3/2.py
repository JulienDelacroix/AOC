offsets = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def n8(x, y):
    for o in [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]:
        yield (x + o[0], y + o[1])

def fill(x, y, o, n):
    for _ in range(n):
        x, y = x + offsets[o][0], y + offsets[o][1]
        v = sum(tracker[p] for p in n8(x, y) if p in tracker)
        tracker.update({(x, y) : v})
        if v > target:
            print(v)
            exit(0)
    return x, y

target = int(input())

tracker = {(0, 0) : 1}
o = x = y = 0
n = 1
while True:
    x, y = fill(x, y, o, n)
    o = (o + 1) % 4

    x, y = fill(x, y, o, n)
    o = (o + 1) % 4

    n += 1
