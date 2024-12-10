from collections import defaultdict

data = list(map(int, input().split(",")))


def compute(signal):
    nb_parameters = [None, 3, 3, 1, 1, 2, 2, 3, 3, 1]
    
    tape = defaultdict(int)
    tape.update({i : v for i, v in enumerate(data)})

    signal_index = 0

    rip, relative_base = 0, 0
    while tape[rip] != 99:
        instr = tape[rip] % 100
        params = [ tape[rip+1+i] for i in range(nb_parameters[instr]) ]
        p_modes = [(tape[rip] % 1000) // 100, (tape[rip] % 10000) // 1000, tape[rip] // 10000 ]

        getp = lambda i: params[i] if p_modes[i] == 1 else tape[params[i] + (relative_base if p_modes[i] == 2 else 0)]
        def setp(i, v):
            tape[params[i] + (relative_base if p_modes[i] == 2 else 0)] = v

        match(instr):
            case 1:
                setp(2, getp(0) + getp(1))
            case 2:
                setp(2, getp(0) * getp(1))
            case 3:
                setp(0, signal[signal_index])
                signal_index += 1
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
            case 9:
               relative_base += getp(0) 
                
        rip += 1 + nb_parameters[instr]


total = 0
for y in range(50):
    for x in range(50):
        res = compute((x, y))
        print(res, end="")
        if res == 1:
            total += 1
    print()
print(total)
