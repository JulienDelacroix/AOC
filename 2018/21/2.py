visited = set()
last = None

r0 = r1 = r2 = r3 = r4 = r5 = 0
while True:
    r5 = r4 | 0x10000                       # 6: bori 4 65536 5
    r4 = 1855046                            # 7: seti 1855046 9 4
    
    while True:                             
        r2 = (r5 & 0xff)                    # 8: bani 5 255 2
        r4 += r2                            # 9: addr 4 2 4
        r4 &= 0xffffff                      #10: bani 4 16777215 4
        r4 *= 65899                         #11: muli 4 65899 4
        r4 &= 0xffffff                      #12: bani 4 16777215 4
        if r5 < 256:                        #13: gtir 256 5 2 / #14: addr 2 3 3
            break                           #16: seti 27 0 3 => 28
        else:                               #15: addi 3 1 3 => 17
            # r2 = 0                        #17: seti 0 9 2
            # while True:
            #     r1 = r2 + 1               #18: addi 2 1 1
            #     r1 *= 256                 #19: muli 1 256 1
            #     if r1 > r5:               #20: gtrr 1 5 1 / #21: addr 1 3 3
            #         break                 #23: seti 25 5 3 => 26
            #     else:                     #22: addi 3 1 3 => 24
            #         r2 += 1               #24: addi 2 1 2
            #                               #25: seti 17 0 3 => 18
            # r5 = r2                       #26: setr 2 7 5
            
            # Note: commented code above is equivalent to integer division by 256
            r5 //= 256
                                            #27: seti 7 9 3 => 8
    if r4 == r0:                            #28: eqrr 4 0 2 / 29: addr 2 3 3
      break                                 # => 31: out of range!

    # track last r4 value before entring loop
    if r4 in visited:
        break
    visited.add(r4)
    last = r4
                                            #30: seti 5 3 3 => 6
print(last)
