import sys

all_replacements = []
replacement_lines, target_lines = sys.stdin.read().split("\n\n")
for line in replacement_lines.splitlines():
    all_replacements.append(line.split(" => "))
molecule = target_lines.splitlines()[0]

generated = set()
for pattern, replacement in all_replacements:
    index = 0
    while True:
        index = molecule.find(pattern, index)
        if index == -1: break
        generated.add(molecule[0:index] + replacement + molecule[index+len(pattern):])
        index += 1

print(len(generated))
