import sys

def fuel(v):
    res = 0
    while True:
        v = v//3 - 2
        if v < 0:
            return res
        res += v
 
print(sum(fuel(int(line)) for line in sys.stdin.read().splitlines()))
