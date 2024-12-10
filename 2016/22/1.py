import sys
import re

input()
input()
nodes = {}
for line in sys.stdin.read().splitlines():
    x, y, s, u = map(int, re.findall(r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T.*", line)[0])
    nodes.update({(x, y) : (s, u)})
    
res = 0
for n1, (s1, u1) in nodes.items():
    for n2, (s2, u2) in nodes.items():
        if n1 == n2: continue
        if 0 < u1 <= (s2-u2):
            res += 1
print(res)
