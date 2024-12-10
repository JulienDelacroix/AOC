import sys
import re

res = 0
for line in sys.stdin.read().splitlines():
    lb, ub, letter, pwd = re.findall(r"(\d+)-(\d+) (\w): (\w+)", line)[0]
    if int(lb) <= pwd.count(letter) <= int(ub):
        res += 1
print(res)
