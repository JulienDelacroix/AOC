import sys
import functools

@functools.lru_cache(None)
def dfs(lastpin, remaining):
    best = 0
    for r in remaining:
        if lastpin in components[r]:
            nextLastPin = components[r][0 if components[r][0] != lastpin else 1]
            best = max(best, sum(components[r]) + dfs(nextLastPin, remaining - frozenset([r])))
    return best

components = []
for line in sys.stdin.read().splitlines():
    components.append(tuple(map(int, line.split("/"))))

print(dfs(0, frozenset(range(len(components)))))
