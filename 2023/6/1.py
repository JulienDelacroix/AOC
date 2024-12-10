import sys
import re

times = map(int, re.findall(r"(\d+)", sys.stdin.readline()))
distances = map(int, re.findall(r"(\d+)", sys.stdin.readline()))

res = 1
for t, d in zip(times, distances):
    res *= sum(1 for i in range(t) if i * (t-i) > d)
print(res)
