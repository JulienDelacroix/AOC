nb_parameters = [None, 3, 3, 1, 1, 2, 2, 3, 3]

def compute(tape):
    rip = 0
    while tape[rip] != 99:
        instr = tape[rip] % 100
        params = [ tape[rip+1+i] for i in range(nb_parameters[instr]) ]
        p_modes = [(tape[rip] % 1000) // 100, (tape[rip] % 10000) // 1000, tape[rip] // 10000 ]

        getp = lambda i: params[i] if p_modes[i] == 1 else tape[params[i]]

        match(instr):
            case 1:
                tape[params[2]] = getp(0) + getp(1)
            case 2:
                tape[params[2]] = getp(0) * getp(1)
            case 3:
                tape[params[0]] = 5
            case 4:
                print(getp(0))
            case 5:
                if getp(0) != 0:
                    rip = getp(1)
                    continue
            case 6:
                if getp(0) == 0:
                    rip = getp(1)
                    continue
            case 7:
                tape[params[2]] = getp(0) < getp(1)
            case 8:
                tape[params[2]] = getp(0) == getp(1)
        
        rip += 1 + nb_parameters[instr]

    return tape[0]

compute(list(map(int, input().split(","))))
