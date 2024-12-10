import sys
import re

moves = input()
rules = {}
for source, left, right in re.findall(r"(\w+) = \((\w+), (\w+)\)", "".join(sys.stdin.readlines())):
    rules.update({ source : (left, right)})

state = "AAA"
n = 0
while state != "ZZZ":
    state = rules[state][moves[n % len(moves)] == 'R']
    n += 1
print(n)
