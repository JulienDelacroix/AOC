import sys

layers = [ tuple(map(int, line.split(": "))) for line in sys.stdin.read().splitlines() ] 
for t in range(10000000):
    res = 0
    if all((t + pos) % (2 * depth - 2) != 0 for pos, depth in layers):
        print(t)
        break
