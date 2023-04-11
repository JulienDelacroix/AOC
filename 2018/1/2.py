import sys
import itertools

f = 0
freq = set()
for c in itertools.cycle(map(int, sys.stdin.read().splitlines())):
    f += c
    if f in freq:
        break
    freq.add(f)
print(f)