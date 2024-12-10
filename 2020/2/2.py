import sys
import re

res = 0
for line in sys.stdin.read().splitlines():
    lb, ub, letter, pwd = re.findall(r"(\d+)-(\d+) (\w): (\w+)", line)[0]
    if sum(pwd[b-1] == letter for b in [int(lb), int(ub)]) == 1:
        res += 1
print(res)
