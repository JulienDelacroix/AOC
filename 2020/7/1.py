import sys
import re
import collections

def solve(current):
    return current == "shiny gold" or any(solve(child) for _, child in graph[current])


graph = collections.defaultdict(list)
for line in sys.stdin.read().splitlines():
    container, contained = line.split(" bags contain ")
    for contained_str in contained.split(","):
        graph[container].extend(map(tuple, re.findall(r"(\d+) (.*) bags?", contained_str)))

print(sum(solve(root) for root in graph.keys()) - 1)
