from collections import defaultdict

regex = input()

stack = []
mindistances = defaultdict(int)

x, y = 0, 0
d = mindistances[(x, y)] = 0

for c in regex:
    match(c):
        case '^': continue
        case '$': continue
        case '(': 
            stack.append((x, y))
            continue
        case '|':
            x, y = stack[-1]
            d = mindistances[(x, y)]
            continue
        case ')':
            x, y = stack.pop()
            d = mindistances[(x, y)]
            continue
        case 'E': x += 1
        case 'W': x -= 1
        case 'N': y -= 1
        case 'S': y += 1
    
    d += 1
    if (x, y) in mindistances:
        d = min(d, mindistances[(x, y)])
    mindistances[(x, y)] = d

print(sum(v >= 1000 for _, v in mindistances.items()))
