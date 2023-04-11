import sys

commands = []
for line in sys.stdin.read().splitlines():
    tokens = line.split()
    if tokens[0] == "cpy":
        commands.append(tokens[2] + " = " + tokens[1])
    elif tokens[0] == "inc":
        commands.append(tokens[1] + " += 1")
    elif tokens[0] == "dec":
        commands.append(tokens[1] + " -= 1")
    else:
        commands.append("i += ((" + tokens[2] + " - 1) if " + tokens[1] + "!= 0 else 0)")

a = b = d = i = 0
c = 1
while i < len(commands):
    exec(commands[i])
    i +=1
print(a)
