import sys

sum = 0
for line in sys.stdin.read().splitlines():
    charlist = [c for c in line if c.isdigit()]
    sum += int("".join([charlist[0], charlist[-1]]))
print(sum)
