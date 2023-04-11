import sys

packages = list(map(int, sys.stdin.read().splitlines()))
capacity = sum(packages) // 3

best = (1000, 0)

def canfill(left, available):
    if left == 0:
        return True
    
    if len(available):
        p = max(available)
        return (p <= left and canfill(left - p, available - {p})) or canfill(left, available - {p})

    return False

def fill(n, q, left, available, discarded):
    global best
    if (n, q) >= best: 
        return
    
    if left == 0 and canfill(capacity, discarded):
        best = min(best, (n, q))

    if len(available):
        p = max(available)
        if p <= left: 
            fill(n + 1, q * p, left - p, available - {p}, discarded)
        fill(n, q, left, available - {p}, discarded | {p})

fill(0, 1, capacity, frozenset(packages), frozenset())
print(best[1])
