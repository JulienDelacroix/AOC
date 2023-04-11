import sys

graph= {}
for line in sys.stdin.read().splitlines():
    source, children = line.split(" <-> ")
    graph.update({int(source) : list(map(int, children.split(", ")))})

visited = set()
q = [0]
visited.add(0)
while len(q):
    v = q.pop()
    for c in graph[v]:
        if c not in visited:
            q.append(c)
            visited.add(c)

print(len(visited))
