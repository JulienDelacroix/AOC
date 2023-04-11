import sys

double = triple = 0
for line in sys.stdin.read().splitlines():
    double += any(line.count(c) == 2 for c in line)
    triple += any(line.count(c) == 3 for c in line)
print(double * triple)
