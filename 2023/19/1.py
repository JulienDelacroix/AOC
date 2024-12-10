import sys
import re

workflows = {}
blocks = list(sys.stdin.read().split("\n\n"))
for line in blocks[0].splitlines():
    name, items = re.findall(r"(\w+){(.*)}", line)[0]
    rules = []
    for rule in items.split(","):
        if ':' in rule:
            test, goto = rule.split(":")
            rules.append((test, goto))
        else:
            default = rule
    workflows.update({name : (tuple(rules), default)})

res = 0
for line in blocks[1].splitlines():
    x, m, a, s = map(int, re.findall(r"(-?\d+)", line))
    w = workflows["in"]

    while True:
        found = False
        rules, default = w
        for test in rules:
            if eval(test[0]):
                name = test[1]
                found = True
                break
        if not found:
            name = default
        if name == "A":
            res += x + m + a + s
            break
        elif name == "R":
            break
        w = workflows[name]

print(res)
