import sys
import re

DECK = 10007
TRACKED = 2019

def new_stack(pos):
    return (2 * DECK - 1 - pos) % DECK

def cut(pos, offset):
    return (DECK - offset + pos) % DECK

def deal(pos, inc):
    return (pos * inc) % DECK

pos = TRACKED
for line in sys.stdin.read().splitlines():
    if line == "deal into new stack":
        pos = new_stack(pos)
    elif line.startswith("cut"):
        offset = int(re.findall(r"-?\d+", line)[0])
        pos = cut(pos, offset)
    else:
        inc = int(re.findall(r"-?\d+", line)[0])
        pos = deal(pos, inc)

print(pos)
