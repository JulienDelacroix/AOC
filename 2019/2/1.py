
tape = list(map(int, input().split(",")))
tape[1] = 12
tape[2] = 2

rip = 0
while tape[rip] != 99:
    params = tape[rip+1:rip+4]
    match(tape[rip]):
        case 1: tape[params[2]] = tape[params[0]] + tape[params[1]]
        case 2: tape[params[2]] = tape[params[0]] * tape[params[1]]
    rip += 4

print(tape[0])
