import sys
import string

commands = []
for line in sys.stdin.read().splitlines():
    tokens = line.split()
    commands.append([tokens[0], tuple(tokens[1:])])

def run(registers):
    rip = res = 0
    while 0 <= rip < len(commands):
        type, args = commands[rip]
        if type == "set":
            registers[args[0]] = int(registers.get(args[1], args[1]))
        elif type == "sub":
            registers[args[0]] -= int(registers.get(args[1], args[1]))
        elif type == "mul":
            registers[args[0]] *= int(registers.get(args[1], args[1]))
            res += 1
        elif type == "jnz":
            if int(registers.get(args[0], args[0])) != 0:
                rip += int(registers.get(args[1], args[1])) - 1
        rip += 1
        print(rip, registers)
    return res

registers = { r : 0 for r in string.ascii_lowercase[0:8] }
print(run(registers))
