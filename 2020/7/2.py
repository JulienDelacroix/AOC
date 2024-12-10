import sys
import re
import collections

def solve(current):
    return 1 + sum(int(count) * solve(child) for count, child in graph[current])


graph = collections.defaultdict(list)
for line in sys.stdin.read().splitlines():
    container, contained = line.split(" bags contain ")
    for contained_str in contained.split(","):
        graph[container].extend(map(tuple, re.findall(r"(\d+) (.*) bags?", contained_str)))

print(solve("shiny gold") - 1)
