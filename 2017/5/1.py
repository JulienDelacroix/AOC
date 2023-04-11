import sys
i = 0
values = list(map(int, sys.stdin.read().splitlines()))

res = 0
while 0 <= i < len(values):
    jump = values[i]
    values[i] += 1
    i += jump
    res += 1
print(res)
