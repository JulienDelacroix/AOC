import sys

containers = list(map(int, sys.stdin.read().splitlines()))

def dfs(indexes, eggnog):
    new_indexes = [i for i in indexes if containers[i] <= eggnog ]

    if eggnog == 0: return 1
    if not new_indexes: return 0
    return dfs(frozenset(new_indexes[1:]), eggnog - containers[new_indexes[0]]) + dfs(frozenset(new_indexes[1:]), eggnog)

print(dfs(range(len(containers)), 150))
