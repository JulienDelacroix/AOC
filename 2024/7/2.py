import sys
from operator import add, mul

def concat(left, right):
    return int(str(left) + str(right))

def solve(wanted, operands, index, current):
    if current > wanted: return False # can only go up[]
    if index == len(operands):
        return current == wanted
    else:
        return any(solve(wanted, operands, index+1, op(current, operands[index])) for op in [add, mul, concat])
    
res = 0
for line in sys.stdin.read().splitlines():
    total_str, operands_str = line.split(": ")
    total, operands = int(total_str), list(map(int, operands_str.split(" ")))
    if solve(total, operands, 0, 0):
        res += total

print(res)
