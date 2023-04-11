import sys

visited = set()
for line in sys.stdin.read().splitlines():
    keys = [(n, line[0:n] + line[n+1:]) for n in range(len(line)) ]
    if any(k in visited for k in keys):
        break 
    visited.update(keys)
print(line)
