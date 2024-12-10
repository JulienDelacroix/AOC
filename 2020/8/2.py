import sys
import re

ops = ["nop", "acc", "jmp"]
pattern = r"(%s) ([+-]\d+)" % ("|". join(ops))

instructions = []
for line in sys.stdin.read().splitlines():
    op, param = re.findall(pattern, line)[0]
    instructions.append((op, int(param)))

def terminate(offset):
    visited = set()
    rip = 0
    accumulator = 0
    while(rip != len(instructions)):
        if rip < 0 or rip > len(instructions) or rip in visited:
            return None
        visited.add(rip)

        op, param = instructions[rip]
        if rip == offset:
            op = {"nop" : "jmp", "acc" : "acc", "jmp" : "nop"}[op]
        match op:
            case "acc":
                accumulator += param
            case "jmp":
                rip += (param - 1)
        rip += 1
    return accumulator
    
    
for offset in range(len(instructions)):
    result = terminate(offset)
    if result is not None:
        print(result)
        break

