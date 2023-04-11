import sys

commands = []
for line in sys.stdin.read().splitlines():
    tokens = line.split()
    commands.append([tokens[0], tuple(tokens[1:])])

for n in range(10000):
    count = 0
    inputs = set()
    a = n
    b = c = d = i = 0
    while i < len(commands):
        type, args = commands[i]
        
        if type == "cpy":
            exec(args[1] + " = " + args[0])
        elif type == "inc":
            exec(args[0] + " += 1")
        elif type == "dec":
            exec(args[0] + " -= 1")
        elif type == "jnz":
            i += ((eval(args[1])- 1) if eval(args[0]) != 0 else 0)
        elif type == "out":
            if b != (count % 2):
                break
            count += 1
            if count % 2 == 0 and (a, b, c, d) in inputs:
                print(n)
                exit()
            inputs.add((a, b, c, d))
        i +=1
