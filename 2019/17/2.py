from collections import defaultdict

nb_parameters = [None, 3, 3, 1, 1, 2, 2, 3, 3, 1]

def compute(data, input_list):
    tape = defaultdict(int)
    tape.update({i : v for i, v in enumerate(data)})

    x = y = 0
    scaffold = set()
    start_pos = None
    input_index = 0

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
                setp(0, input_list[input_index])
                print(chr(input_list[input_index]), end="")
                input_index += 1
            case 4:
                v = getp(0)
                if v > 255:
                    print(v)
                    exit(0)

                print(chr(v), end="")
                if v == 10:
                    x, y = 0, y+1
                else:
                    if chr(v) == '#':
                        scaffold.add((x, y))
                    if chr(v) == '^':
                        start_pos = (x, y)
                    x += 1
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
    return scaffold, start_pos


def n4(pos): 
    x, y = pos
    yield (x, y-1)
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y+1)

def generate_moves(scaffold, start_pos):
    x, y = start_pos
    dir = 3 # dir = RDLU

    # compute path
    moves = []
    while True:
        # try moving ahead
        nx, ny = ((x+1, y), (x, y+1), (x-1, y), (x, y-1))[dir]
        if (nx, ny) in scaffold:
            x, y = nx, ny
            moves[-1] += 1
            continue
        
        # try turning right
        nx, ny = ((x+1, y), (x, y+1), (x-1, y), (x, y-1))[(dir+1) % 4]
        if (nx, ny) in scaffold:
            dir = (dir+1) % 4
            moves.extend(['R', 0])
            continue
        
        # try turning left
        nx, ny = ((x+1, y), (x, y+1), (x-1, y), (x, y-1))[(dir+3) % 4]
        if (nx, ny) in scaffold:
            dir = (dir+3) % 4
            moves.extend(['L', 0])
            continue
        
        return ",".join(map(str, moves))
        
    
def decompose(pattern, tokens):
    if len(tokens) > 3: return None
    if len(tokens) == 3 and len(pattern) == 0: return tokens
        
    for s in range(0, len(pattern)+1):
        if (s == len(pattern) or pattern[s] == ',') and s <= 20:
            res = decompose(pattern[s+1:], tokens | frozenset( [pattern[:s]]))
            if res:
                return res
    return None


data = list(map(int, input().split(",")))
scaffold, start_pos = compute(data, None)

# compute functions
moves = generate_moves(scaffold, start_pos)
functions = decompose(moves, frozenset())

# compute main routine
main_routine = moves
for n, func in enumerate(functions):
    main_routine = main_routine.replace(func, "ABC"[n])

# generate input
input_list = list(map(ord, main_routine))
input_list.append(10)
for func in functions:
    input_list.extend(map(ord, func))
    input_list.append(10)
input_list.extend([ ord('n'), 10 ])

# let's go!
data[0] = 2
compute(data, input_list)
