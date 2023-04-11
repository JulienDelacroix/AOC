import sys

res = 0
for line in sys.stdin.read().splitlines():
    values = list(map(int, line.split()))
    print(values)
    res += max(values) - min(values)
print(res)
