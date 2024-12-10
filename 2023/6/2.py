import sys
import re

t = int("".join(re.findall(r"(\d+)", sys.stdin.readline())))
d = int("".join(re.findall(r"(\d+)", sys.stdin.readline())))
print(sum(1 for i in range(t) if i * (t-i) > d))
