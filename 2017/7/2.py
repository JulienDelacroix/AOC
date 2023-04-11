import sys
from collections import Counter

programs = {}
referenced = set() 

def weight(p):
    return programs[p][0] + sum(weight(c) for c in programs[p][1])

def check(p, target):
    _, children = programs[p]
    count = Counter(weight(c) for c in children)
    balanced = count.most_common()[0][0]
    if len(count.most_common()) == 1:
        print(target - sum(weight(c) for c in children))
        exit(0)
    for c in children:
        if weight(c) != balanced:
            check(c, balanced)
 
for line in sys.stdin.read().splitlines():
    tokens = line.split(" -> ")
    name, size = tokens[0].split()
    programs.update({ name : [int(size[1:-1]), []]})
    if len(tokens) > 1:
        children = tokens[1].split(", ")
        programs[name][1] = children
        referenced.update(children)

root = tuple(programs.keys() - referenced)[0]
check(root, 0)
