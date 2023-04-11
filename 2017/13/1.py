import sys

res = 0
for line in sys.stdin.read().splitlines():
    pos, depth = map(int, line.split(": "))
    if pos % (2 * depth - 2) == 0:
        res += pos * depth
print(res)
