import sys

REGISTERS = ("a", "b", "f", "i", "p")
#REGISTERS = ("a", "b", "c", "d", "p") # for test input

commands = []
for line in sys.stdin.read().splitlines():
    tokens = line.split()
    commands.append([tokens[0], tuple(tokens[1:])])

rip = 0
registers = { r : 0 for r in REGISTERS }
played = recovered = 0

while 0 <= rip < len(commands):
    type, args = commands[rip]
    if type == "snd":
        played = int(registers.get(args[0], args[0]))
    elif type == "set":
        registers[args[0]] = int(registers.get(args[1], args[1]))
    elif type == "add":
        registers[args[0]] += int(registers.get(args[1], args[1]))
    elif type == "mul":
        registers[args[0]] *= int(registers.get(args[1], args[1]))
    elif type == "mod":
        registers[args[0]] %= int(registers.get(args[1], args[1]))
    elif type ==  "rcv":
        if registers.get(args[0], args[0]):
            print(played)
            exit(0)
    elif type ==  "jgz":
        if int(registers.get(args[0], args[0])) > 0:
            rip += int(registers.get(args[1], args[1])) - 1
    rip += 1
