import sys

res = 0
for line in sys.stdin.read().splitlines():
    dims = list(map(int, line.split("x")))
    l, w, h = dims
    res += l * w * h
    res += 2 * (sorted(dims)[0] + sorted(dims)[1])
print(res)
