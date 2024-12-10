import sys
import math
import itertools

numbers = list(map(int, sys.stdin.read().splitlines()))
print(next(math.prod(n) for n in itertools.product(numbers, repeat=2) if sum(n) == 2020))
