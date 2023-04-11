import itertools
nb_parameters = [None, 3, 3, 1, 1, 2, 2, 3, 3]

def compute(tape, phase, signal):
    rip = 0
    read = 0
    while tape[rip] != 99:
        instr = tape[rip] % 100
        params = [ tape[rip+1+i] for i in range(nb_parameters[instr]) ]
        p_modes = [(tape[rip] % 1000) // 100, (tape[rip] % 10000) // 1000, tape[rip] // 10000 ]

        getp = lambda i: params[i] if p_modes[i] == 1 else tape[params[i]]
        def setp(i, v):
            tape[params[i]] = v

        match(instr):
            case 1:
                setp(2, getp(0) + getp(1))
            case 2:
                setp(2, getp(0) * getp(1))
            case 3:
                setp(0, phase if read == 0 else signal)
                read += 1
            case 4:
                return getp(0)
            case 5:
                if getp(0) != 0:
                    rip = getp(1)
                    continue
            case 6:
                if getp(0) == 0:
                    rip = getp(1)
                    continue
            case 7:
                setp(2, getp(0) < getp(1))
            case 8:
                setp(2, getp(0) == getp(1))
        
        rip += 1 + nb_parameters[instr]

    return tape[0]


data = list(map(int, input().split(",")))
res = 0
for phase in itertools.permutations(range(5)):
    signal = 0
    for index in range(5):
        signal = compute([d for d in data], phase[index], signal)
    res = max(res, signal)
print(res)
