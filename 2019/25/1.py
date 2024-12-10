from collections import defaultdict

input_file = open("input", 'r')
data = list(map(int, input_file.read().split(",")))


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
                if signal_index == len(signal):
                    signal = list(input())
                    signal.append("\n")
                    signal_index = 0
                setp(0, ord(signal[signal_index]))
                signal_index += 1
            case 4:
                if getp(0) > 127:
                    print(getp(0))
                else:
                    print(chr(getp(0)), end="")
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

# Take items:
# - klein bottle
# - mutex
# - hypercube
# - mug
