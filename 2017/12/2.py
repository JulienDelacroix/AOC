import sys

graph= {}
for line in sys.stdin.read().splitlines():
    source, children = line.split(" <-> ")
    graph.update({int(source) : list(map(int, children.split(", ")))})

res = 0
visited = set()
for start in graph.keys():
    if start in visited: continue
    res += 1
    q = [start]
    visited.add(start)
    while len(q):
        v = q.pop()
        for c in graph[v]:
            if c not in visited:
                q.append(c)
                visited.add(c)

print(res)
