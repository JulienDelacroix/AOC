import sys
import itertools
import math

numbers = list(map(int, sys.stdin.read().splitlines()))
print(next(math.prod(n) for n in itertools.product(numbers, repeat=3) if sum(n) == 2020))
