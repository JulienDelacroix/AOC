import sys

res = 0
for line in sys.stdin.read().splitlines():
    a, b, c = list(sorted(map(int, line.split())))
    if a + b > c:
        res += 1
print(res)
    