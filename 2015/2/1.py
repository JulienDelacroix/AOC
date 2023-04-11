import sys

res = 0
for line in sys.stdin.read().splitlines():
    dims = list(map(int, line.split("x")))
    l, w, h = dims
    res += 2*l*w + 2*w*h + 2*h*l
    res += sorted(dims)[0] * sorted(dims)[1]
print(res)
