from collections import defaultdict
from queue import Queue

nb_parameters = [None, 3, 3, 1, 1, 2, 2, 3, 3, 1]

def compute(tape, rip, relative_base, signal):
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
                return tape, rip + 1 + nb_parameters[instr], relative_base, getp(0)
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

q = Queue()
q.put(((0, 0), 0, tape, 0, 0))

explored = set()
explored.add((0, 0))

elapsed_time = 0
while not q.empty():
    (x, y), nb_moves, tape, rip, relative_base = q.get()
    elapsed_time = max(elapsed_time, nb_moves)
    
    for dir, npos in enumerate([(x, y-1), (x, y+1), (x-1, y), (x+1, y)]):
        if npos not in explored:
            new_tape, rip, relative_base, res = compute(dict(tape), rip, relative_base, dir+1)
            explored.add(npos)
            match(res):
                case 1:
                    q.put((npos, nb_moves+1, new_tape, rip, relative_base))
                case 2:
                    q = Queue()
                    q.put((npos, 0, new_tape, rip, relative_base))
                    explored = set([ npos])

print(elapsed_time)
