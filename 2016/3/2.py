import sys

res = 0
inputs = [ list(map(int, line.split())) for line in sys.stdin.read().splitlines() ]
for i in range(0, len(inputs), 3):
    for a, b, c in map(sorted, zip(inputs[i], inputs[i+1], inputs[i+2])):
        if a + b > c:
            res += 1
print(res)
