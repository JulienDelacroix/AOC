import sys
import re

all_oppcodes = [
    "addr", "addi", 
    "mulr", "muli", 
    "banr", "bani", 
    "borr", "bori", 
    "setr", "seti", 
    "gtir", "gtri", "gtrr",
    "eqir", "eqri", "eqrr"
]
def apply(instruction, registers):
    oppcode, a, b, c = instruction
    result = [v for v in registers]
    match oppcode:
        case "addr": result[c] = registers[a] + registers[b]
        case "addi": result[c] = registers[a] + b

        case "mulr": result[c] = registers[a] * registers[b]
        case "muli": result[c] = registers[a] * b

        case "banr": result[c] = registers[a] & registers[b]
        case "bani": result[c] = registers[a] & b

        case "borr": result[c] = registers[a] | registers[b]
        case "bori": result[c] = registers[a] | b

        case "setr": result[c] = registers[a]
        case "seti": result[c] = a

        case "gtir": result[c] = 1 if a > registers[b] else 0
        case "gtri": result[c] = 1 if registers[a] > b else 0
        case "gtrr": result[c] = 1 if registers[a] > registers[b] else 0

        case "eqir": result[c] = 1 if a == registers[b] else 0
        case "eqri": result[c] = 1 if registers[a] == b else 0
        case "eqrr": result[c] = 1 if registers[a] == registers[b] else 0
    return result


rip_register = int(re.findall(r"(\d+)", input())[0])

instructions = []
for line in sys.stdin.read().splitlines():
    tokens = re.findall(r"(\w+) (\d+) (\d+) (\d+)", line)[0]
    oppcode = tokens[0]
    params = list(map(int, tokens[1:]))
    instructions.append([oppcode] + params)

registers = [0] * 6
rip = 0
while 0 <= rip < len(instructions):
    instr = instructions[rip]
    registers = apply(instr, registers)
    registers[rip_register] += 1
    rip = registers[rip_register]
    print(registers)
    if instr == ["eqrr", 4, 0, 2]:
        print(registers[4])
        break
