import sys

all_replacements = []
replacement_lines, target_lines = sys.stdin.read().split("\n\n")
for line in replacement_lines.splitlines():
    all_replacements.append(line.split(" => "))
all_replacements = [(r, p) for p, r in all_replacements]
all_replacements.sort(key = lambda x: -len(x[0]))
target = target_lines.splitlines()[0]

best = 10000

def dfs(molecule, depth):
    global best
    if molecule == "e":
        best = min(best, depth)
        return

    if (len(molecule) + depth) > best: return

    for pattern, replacement in all_replacements:
        index = 0
        while True:
            index = molecule.find(pattern, index)
            if index == -1: break
            dfs(molecule[0:index] + replacement + molecule[index+len(pattern):], depth + 1)
            index += 1


dfs(target, 0)
print(best)
