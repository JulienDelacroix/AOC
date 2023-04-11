import sys
import itertools

res = 0
for line in sys.stdin.read().splitlines():
    values = list(map(int, line.split()))
    res += sum(v2 // v1 for v1, v2 in itertools.combinations(sorted(values), 2) if v2 % v1 == 0)
print(res)
