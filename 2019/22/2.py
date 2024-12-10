import sys
import re

DECK = 119315717514047
TRACKED = 2020
REPEAT = 101741582076661

def new_stack(pos):
    return (2 * DECK - 1 - pos) % DECK

def cut(pos, offset):
    return (DECK - offset + pos) % DECK

def deal(pos, inc):
    return (pos * inc) % DECK

def shuffle(pos, instructions):
    for line in instructions:
        if line == "deal into new stack":
            pos = new_stack(pos)
        elif line.startswith("cut"):
            offset = int(re.findall(r"-?\d+", line)[0])
            pos = cut(pos, offset)
        else:
            inc = int(re.findall(r"-?\d+", line)[0])
            pos = deal(pos, inc)
    return pos


def modularProd(left, right):
    res = []
    for y in range(2):
        res.append([])
        for x in range(2):
            val = 0
            for i in range(2):
                val += (left[y][i] * right[i][x]) % DECK
                val %= DECK
            res[y].append(val)
    return res
        
def fastExponentiation(val, power):
    if power == 1:
        return val
    
    if power % 2 == 0:
        return fastExponentiation(modularProd(val, val), power//2)
    else:
        return modularProd(val, fastExponentiation(val, power-1))


instructions = sys.stdin.read().splitlines()
pos1, pos2 = 42, 666
shuffled1, shuffled2 = shuffle(pos1, instructions), shuffle(pos2, instructions)

# Note: all operations involved in shuffling are linear operations in Z/pZ with p prime
# Thus there exists a and b such that:
#   a * shuffled1 + b = pos1 [mod DECK]
#   a * shuffled2 + b = pos2 [mod DECK]
a = ((pos1 - pos2) * pow(shuffled1 - shuffled2, -1, DECK)) % DECK
b1 = (DECK + pos1 - (a * shuffled1)) % DECK
b2 = (DECK + pos2 - (a * shuffled2)) % DECK
assert b1 == b2

# In matrix form
unshuffle_once = [[a, b1], [0, 1]]
unshuffle = fastExponentiation(unshuffle_once, REPEAT)

print((unshuffle[0][0] * TRACKED + unshuffle[0][1]) % DECK)
