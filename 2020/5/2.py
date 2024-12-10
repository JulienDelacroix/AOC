import sys

all_seats = set()
for line in sys.stdin.read().splitlines():
    row = sum((1 if digit == 'B' else 0) * pow(2, pos) for pos, digit in enumerate(reversed(line[:7])))
    col = sum((1 if digit == 'R' else 0) * pow(2, pos) for pos, digit in enumerate(reversed(line[7:])))
    seat = row * 8 + col
    all_seats.add(seat)

for s in all_seats:
    if s-2 in all_seats and s-1 not in all_seats:
        print(s-1)
        break
    