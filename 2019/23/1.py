from collections import defaultdict
import itertools

from dataclasses import dataclass

nb_parameters = [None, 3, 3, 1, 1, 2, 2, 3, 3, 1]

def compute(tape, rip, relative_base, signal):
    out = []

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
                if len(signal):
                    setp(0, signal[0])
                    signal = signal[1:]
                else:
                    setp(0, -1)
                    return tape, rip + 1 + nb_parameters[instr], relative_base, out
                    
            case 4:
                out.append(getp(0))
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
    return None, None, None, None

data = map(int, input().split(","))
tape = defaultdict(int)
tape.update({i : v for i, v in enumerate(data)})

@dataclass 
class State:
    tape: dict
    rip: int
    relative_base: int
    queue: list
    
all_states = [State(tape, 0, 0, [d]) for d in range(50)]

while True:
    for state in all_states:
        state.tape, state.rip, state.relative_base, output = compute(dict(state.tape), state.rip, state.relative_base, state.queue)
        state.queue = []
        for packet in itertools.batched(output, 3):
            c, x, y = packet
            if c == 255:
                print(y)
                exit()
            else:
                all_states[c].queue.extend([x, y])
