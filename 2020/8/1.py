import sys
import re

ops = ["nop", "acc", "jmp"]
pattern = r"(%s) ([+-]\d+)" % ("|". join(ops))

instructions = []
for line in sys.stdin.read().splitlines():
    op, param = re.findall(pattern, line)[0]
    instructions.append((op, int(param)))

visited = set()
rip = 0
accumulator = 0
while(True):
    if rip in visited:
        break
    visited.add(rip)

    op, param = instructions[rip]
    match op:
        case "acc":
            accumulator += param
        case "jmp":
            rip += (param - 1)
    rip += 1
print(accumulator)
