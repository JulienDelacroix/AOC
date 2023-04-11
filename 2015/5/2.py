import sys

res = 0
for s in sys.stdin.read().splitlines():
    if (sum(s[i:i+2] in s[i+2:] for i in range(len(s)-2)) == 0): continue
    if (sum(s[i] == s[i+2] for i in range(len(s)-2)) == 0): continue    
    res += 1
print(res)
