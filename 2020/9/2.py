import sys
import itertools

PREAMBLE = 25

numbers = list(map(int, sys.stdin.read().splitlines()))

for offset, num in enumerate(numbers[PREAMBLE:]):
    preamble = numbers[offset : offset + PREAMBLE]
    if not any(n1 + n2 == num for n1, n2 in itertools.combinations(preamble, r=2)):
        break

total = 0
first = last = 0
while total != num:
    if total < num:
        total += numbers[last]
        last += 1
    if total > num:
        total -= numbers[first]
        first += 1
    
print(min(numbers[first:last]) + max(numbers[first:last]))
