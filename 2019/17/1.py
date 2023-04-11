from collections import defaultdict

nb_parameters = [None, 3, 3, 1, 1, 2, 2, 3, 3, 1]

def n4(pos): 
    x, y = pos
    yield (x, y-1)
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y+1)

def compute(data):
    tape = defaultdict(int)
    tape.update({i : v for i, v in enumerate(data)})

    x = y = 0
    picture = set()

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
                setp(0, None)
            case 4:
                v = getp(0)
                if v == 10:
                    x, y = 0, y+1
                else:
                    if chr(v) == '#':
                        picture.add((x, y))
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
    return picture


picture = compute(map(int, input().split(",")))

intersections = [ pos for pos in picture if sum(npos in picture for npos in n4(pos)) == 4 ]
print(sum(x *y for x, y in intersections))