import sys

delimiters = { ')' : '(', ']' : '[', '}' : '{', '>' : '<' }
values = { '(' : 1, '[' : 2, '{' : 3, '<' : 4 }

scores = []
for line in sys.stdin.read().splitlines():
    q = []
    for c in line:
        if c in delimiters:
            if q.pop() != delimiters[c]:
                break
        else:
            q.append(c)
    else:
        s = 0
        for opened in reversed(q):
            s = 5 * s + values[opened]
        scores.append(s)

print(sorted(scores)[len(scores)//2])
