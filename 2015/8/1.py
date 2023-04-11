import sys

print(sum(len(line) - len(eval(line)) for line in sys.stdin.read().splitlines()))
