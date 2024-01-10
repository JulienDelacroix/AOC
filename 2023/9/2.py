import sys

def solve(s):
    if len(s) == 0: 
        return 0
    return s[0] - solve([s[i]-s[i-1] for i in range(1, len(s))])

print(sum(solve(list(map(int, line.split()))) for line in sys.stdin.read().splitlines()))
