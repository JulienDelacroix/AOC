import sys

delimiters = { ')' : '(', ']' : '[', '}' : '{', '>' : '<' }
values = { ')' : 3, ']' : 57, '}' : 1197, '>' : 25137 }

res = 0
for line in sys.stdin.read().splitlines():
    q = []
    for c in line:
        if c in delimiters:
            if q.pop() != delimiters[c]:
                res += values[c]
                break
        else:
            q.append(c)

print(res)