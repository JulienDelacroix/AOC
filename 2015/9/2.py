import sys
import re
import functools

distances = {}

@functools.lru_cache(None)
def dfs(last, remaining):
    if len(remaining) == 0:
        return 0
    return max((distances[(last, town)] if last else 0) + dfs(town, remaining - {town}) for town in remaining)

all_towns = set()
for line in sys.stdin.read().splitlines():
    source, dest, dist = re.findall("(.*) to (.*) = (\d+)", line)[0]
    distances.update({(source, dest) : int(dist), (dest, source) : int(dist)})
    all_towns.add(source)
    all_towns.add(dest)
    print(source, dest, dist)

print(dfs(None, frozenset(all_towns)))
