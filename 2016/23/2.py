import sys

def toggle(command):
    type, args = command
    if len(args) == 1: command[0] = "dec" if type == "inc" else "inc"
    if len(args) == 2: command[0] = "cpy" if type == "jnz" else "jnz"

commands = []
for line in sys.stdin.read().splitlines():
    tokens = line.split()
    commands.append([tokens[0], tuple(tokens[1:])])

a = 12
b = c = d = i = 0

while i < len(commands):
    type, args = commands[i]

    if i == 5:
        a += c * d
        c = d = 0
        i = 9 
    elif type == "cpy":
        exec(args[1] + " = " + args[0])
    elif type == "inc":
        exec(args[0] + " += 1")
    elif type == "dec":
        exec(args[0] + " -= 1")
    elif type == "jnz":
        i += ((eval(args[1])- 1) if eval(args[0]) != 0 else 0)
    elif type == "tgl":
        offset = eval(args[0])
        if 0 <= i+offset < len(commands):
            toggle(commands[i+offset])
    i +=1
print(a)
