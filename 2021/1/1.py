import sys

values = map(int, sys.stdin.read().splitlines())
print(sum(1 for v1, v2 in zip(values, values[1:]) if v2 > v1))
