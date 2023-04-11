import sys
import re
import math

moves = input()
rules = {}
for source, left, right in re.findall("(\w+) = \((\w+), (\w+)\)", "".join(sys.stdin.readlines())):
    rules.update({ source : (left, right)})

states = [source for source in rules.keys() if source[-1] == 'A']
steps = []
for s in states:
    n = 0
    while s[-1] != 'Z':
        s = rules[s][moves[n % len(moves)] == 'R']
        n += 1
    steps.append(n)

print(math.lcm(*steps))
