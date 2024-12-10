import sys

combined = [tuple(map(int, line.split())) for line in sys.stdin.read().splitlines()]
list1, list2 = sorted(t[0] for t in combined), sorted(t[1] for t in combined)
print(sum(n * list2.count(n) for n in list1))
