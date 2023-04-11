import itertools
from dataclasses import dataclass

@dataclass
class Amplifier:
    tape: list
    rip: int

nb_parameters = [None, 3, 3, 1, 1, 2, 2, 3, 3]

def compute(tape, rip, signal, init=False):
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
                setp(0, signal)
                if init:
                    return rip + 1 + nb_parameters[instr], None
            case 4:
                return rip + 1 + nb_parameters[instr], getp(0)
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

    return None, None


res = 0
data = list(map(int, input().split(",")))
for phase in itertools.permutations(range(5, 10)):
    amplifiers = [ Amplifier([d for d in data], 0) for _ in range(5) ]
    for n, a in enumerate(amplifiers):
        a.rip, _ = compute(a.tape, a.rip, phase[n], init=True)

    n = signal = 0
    while amplifiers[n].rip is not None:
        if n == 0:
            res = max(res, signal)
        amplifiers[n].rip, signal = compute(amplifiers[n].tape, amplifiers[n].rip, signal)
        n = (n + 1) % 5

print(res)    
