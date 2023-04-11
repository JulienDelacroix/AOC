import sys

values = map(int, sys.stdin.read().splitlines())
sums = [v1+v2+v3 for v1,v2,v3 in zip(values, values[1:], values[2:])]
print(sum(1 for s1, s2 in zip(sums, sums[1:]) if s2 > s1))
