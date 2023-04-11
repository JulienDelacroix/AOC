import sys

REGISTERS = ("a", "b", "f", "i", "p")
#REGISTERS = ("a", "b", "c", "d", "p") # for test input

commands = []
for line in sys.stdin.read().splitlines():
    tokens = line.split()
    commands.append([tokens[0], tuple(tokens[1:])])

def run(recv_queue, state):
    sent, received, rip, registers = state
    while 0 <= rip < len(commands):
        type, args = commands[rip]
        if type == "snd":
            sent.append(int(registers.get(args[0], args[0])))
        elif type == "set":
            registers[args[0]] = int(registers.get(args[1], args[1]))
        elif type == "add":
            registers[args[0]] += int(registers.get(args[1], args[1]))
        elif type == "mul":
            registers[args[0]] *= int(registers.get(args[1], args[1]))
        elif type == "mod":
            registers[args[0]] %= int(registers.get(args[1], args[1]))
        elif type ==  "rcv":
            if received < len(recv_queue):
                registers[args[0]] = recv_queue[received]
                received += 1
            else:
                return (sent, received, rip, registers)
        elif type ==  "jgz":
            if int(registers.get(args[0], args[0])) > 0:
                rip += int(registers.get(args[1], args[1])) - 1
        rip += 1
    return (sent, received, rip, registers)


states = [([], 0, 0, { r : 0 for r in REGISTERS }), ([], 0, 0, { r : 0 for r in REGISTERS })]
states[1][3]["p"] = 1

last_sent = 0
while True:
    sent = 0
    for p in (0, 1):
        states[p] = run(states[1-p][0], states[p])
        sent += len(states[p][0])
    if sent == last_sent:
        break
    last_sent = sent

print(len(states[1][0]))

