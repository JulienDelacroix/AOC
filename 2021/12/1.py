import sys

graph = {}
def update_graph(source, dest):
    if source not in graph:
        graph.update({ source : [dest]})
    else:
        graph[source].append(dest)

def dfs(pos, visited):
    if pos == "end": return 1

    result = 0
    for next_pos in graph[pos]:
        if next_pos.isupper() or next_pos not in visited:
            result += dfs(next_pos, visited | frozenset([pos]))
    return result 

for line in sys.stdin.read().splitlines():
    source, dest = tuple(line.split("-"))
    update_graph(source, dest)
    update_graph(dest, source)

print(dfs("start", frozenset()))


