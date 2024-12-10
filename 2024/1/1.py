import sys

combined = [tuple(map(int, line.split())) for line in sys.stdin.read().splitlines()]
list1, list2 = sorted(t[0] for t in combined), sorted(t[1] for t in combined)
print(sum(abs(v1 - v2) for v1, v2 in zip(list1, list2)))
