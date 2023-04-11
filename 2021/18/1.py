import sys
import functools

def add_left(n, val):
    return n+val if isinstance(n, int) else [add_left(n[0], val), n[1]]

def add_right(n, val):
    return n+val if isinstance(n, int) else [n[0], add_right(n[1], val)]

def explode(n, depth):
    if isinstance(n, int): return False, 0, n, 0

    if depth < 4:
        updated, left, res, right = explode(n[0], depth+1)
        if updated: return True, left, [res, add_left(n[1], right)], 0

        updated, left, res, right = explode(n[1], depth+1)
        if updated: return True, 0, [add_right(n[0], left), res], right

        return False, 0, n, 0

    return True, n[0], 0, n[1]

def split(n):
    if isinstance(n, int): return (True, [n//2, n - n//2]) if n>=10 else (False, n)
    
    updated, res = split(n[0])
    if updated: return True, [res, n[1]] 
    
    updated, res = split(n[1])
    if updated: return True, [n[0], res]

    return False, n

def magnitude(n):
    return n if isinstance(n, int) else (3 * magnitude(n[0]) + 2 * magnitude(n[1]))

def add(l1, l2):
    res = [l1, l2]
    while True:
        updated, _, res, _ = explode(res, 0)
        if updated: continue
        
        updated, res = split(res)
        if updated: continue
        
        break
    return res

numbers = []
for line in sys.stdin.read().splitlines():
    numbers.append(eval(line))

print(magnitude(functools.reduce(lambda r, v: add(r,v), numbers)))
