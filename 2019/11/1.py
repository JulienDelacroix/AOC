from collections import defaultdict

nb_parameters = [None, 3, 3, 1, 1, 2, 2, 3, 3, 1]

def compute(tape, rip, relative_base, signal):
    output = []
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
                setp(0, signal)
            case 4:
                output.append(getp(0))
                if len(output) == 2:
                    return rip + 1 + nb_parameters[instr], relative_base, output
            case 5:
                if getp(0) != 0:
                    rip = getp(1)
                    continue
            case 6:
                if getp(0) == 0:
                    rip = getp(1)
                    continue
            case 7:
                setp(2, 1 if getp(0) < getp(1) else 0)
            case 8:
                setp(2, 1 if getp(0) == getp(1) else 0)
            case 9:
               relative_base += getp(0) 
                
        rip += 1 + nb_parameters[instr]
    return None, None, None

data = map(int, input().split(","))
tape = defaultdict(int)
tape.update({i : v for i, v in enumerate(data)})

pannels = defaultdict(int)
rip = relative_base = x = y = 0
dir = 3 # "RDLU"

while True:
    rip, relative_base, output = compute(tape, rip, relative_base, pannels[(x, y)])
    if rip is None: 
        break
    
    color, turn = output
    pannels[(x, y)] = color
    dir = (dir + (3 if turn == 0 else 1)) % 4
    x, y = ((x+1, y), (x, y+1), (x-1, y), (x, y-1))[dir]
    
print(len(pannels))
