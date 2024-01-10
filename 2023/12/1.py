import sys

def solve(s, a):
    if not s: return not a
    if not a: return '#' not in s
    
    match = 0
    if len(s) > a[0] and '.' not in s[:a[0]] and s[a[0]] != '#':
        match += solve(s[a[0]+1:], a[1:])
    if s[0] != '#':
        match += solve(s[1:], a)
    return match

res = 0    
for line in sys.stdin.read().splitlines():
    s1, s2 = line.split(" ")

    springs = s1 + "."
    arr = tuple(map(int, s2.split(",")))
    res += solve(springs, arr)

print(res)
