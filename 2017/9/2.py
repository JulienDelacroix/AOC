stream = input()

skip = garbage = False
res = 0
for c in stream:
    if garbage:
        if skip:
            skip = False
        elif c == '!':
            skip = True
        elif c == '>':
            garbage = False
        else:
            res += 1
    else:
        if c == '<':
            garbage = True

print(res)
