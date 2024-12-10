import sys
import re

picture, moves = sys.stdin.read().split("\n\n")

lines = picture.splitlines()
stacks = [[v for v in reversed(list(x)) if v.isalpha()] for x in list(zip(*lines)) if x[-1].isnumeric()]

for m in moves.splitlines():
    amount, source, dest = map(int, re.findall(r"\d+", m))
    tmp = []
    for i in range(amount):
        tmp.append(stacks[source-1].pop())
    for i in range(amount):
        stacks[dest-1].append(tmp.pop())

print("".join( [ s[-1] for s in stacks if s]))
