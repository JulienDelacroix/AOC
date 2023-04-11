from collections import defaultdict

nb_parameters = [None, 3, 3, 1, 1, 2, 2, 3, 3, 1]

def compute(data):
    tape = defaultdict(int)
    tape.update({i : v for i, v in enumerate(data)})
    tape[0] = 2

    output = []
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
                move = -1 if ball < paddle else (1 if ball > paddle else 0)
                setp(0, move)
            case 4:
                output.append(getp(0))
                if len(output) == 3:
                    if output[0] == -1:
                        score = output[2]
                        print("\033[26;2H SCORE: \033[0m" + str(output[2]))
                    else:
                        if output[2] == 4:
                            ball = output[0]
                        if output[2] == 3:
                            paddle = output[0]
                   
                        # let's have some fun :-D
                        import time
                        time.sleep(0.005)
                        display = [ "\033[0m ", "\033[1;31m#", "\033[34;7m ", "\033[1;32m-", "\033[1;32mo"]
                        print("\033[" + str(output[1]+1) + ";" + str(output[0]+1) + "H" + display[output[2]])
                       
                    output.clear()
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
    return score


print("\033[2J") # clear screen before the fun begin
compute(map(int, input().split(",")))
