import sys
from collections import Counter

containers = list(map(int, sys.stdin.read().splitlines()))
tracker = Counter()

def dfs(indexes, used, eggnog):
    new_indexes = [i for i in indexes if containers[i] <= eggnog ]

    if eggnog == 0: tracker[used] += 1
    if not new_indexes: return

    dfs(frozenset(new_indexes[1:]), used + 1, eggnog - containers[new_indexes[0]])
    dfs(frozenset(new_indexes[1:]), used, eggnog)

dfs(range(len(containers)), 0, 150)
print(tracker[min(tracker.keys())])
