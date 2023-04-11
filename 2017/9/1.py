stream = input()

skip = garbage = False
res = depth = 0
for c in stream:
    if garbage:
        if skip:
            skip = False
        elif c == '!':
            skip = True
        elif c == '>':
            garbage = False
    else:
        if c == '{':
            depth += 1
            res += depth
        elif c == '}':
            depth -= 1
        elif c == '<':
            garbage = True

print(res)
