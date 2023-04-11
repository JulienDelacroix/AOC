import sys

def count(expr):
    if isinstance(expr, int): 
        return expr
    if isinstance(expr, list):
        return sum(count(v) for v in expr)
    if isinstance(expr, dict):
        return sum(count(k) + count(v) for k, v in expr.items())
    return 0

print(sum(count(eval(line)) for line in sys.stdin.read().splitlines()))
