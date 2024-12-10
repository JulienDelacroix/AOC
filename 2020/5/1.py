import sys

res = 0
for line in sys.stdin.read().splitlines():
    row = sum((1 if digit == 'B' else 0) * pow(2, pos) for pos, digit in enumerate(reversed(line[:7])))
    col = sum((1 if digit == 'R' else 0) * pow(2, pos) for pos, digit in enumerate(reversed(line[7:])))
    seat = row * 8 + col
    res = max(res, seat)
print(res)    
