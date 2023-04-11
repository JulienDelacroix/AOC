import sys

res = 0
for s in sys.stdin.read().splitlines():
    if sum(c in "aeiou" for c in s) < 3: continue
    if all(s[i] != s[i+1] for i in range(len(s)-1)): continue
    if any(forbidden in s for forbidden in ("ab", "cd", "pq", "xy")): continue
    res += 1
print(res)
