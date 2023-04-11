def compute(tape, noun, verb):
    tape[1] = noun
    tape[2] = verb

    rip = 0
    while tape[rip] != 99:
        params = tape[rip+1:rip+4]
        match(tape[rip]):
            case 1: tape[params[2]] = tape[params[0]] + tape[params[1]]
            case 2: tape[params[2]] = tape[params[0]] * tape[params[1]]
        rip += 4

    return tape[0]

data = list(map(int, input().split(",")))
for noun in range(100):
    for verb in range(100):
        if compute([d for d in data], noun, verb) == 19690720:
            print(100 * noun + verb)
            exit(0)
