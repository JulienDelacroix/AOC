import sys
import re
import functools
import operator

workflows = {}
blocks = list(sys.stdin.read().split("\n\n"))
for line in blocks[0].splitlines():
    name, items = re.findall(r"(\w+){(.*)}", line)[0]
    rules = []
    for rule in items.split(","):
        if ':' in rule:
            test, goto = rule.split(":")
            rules.append((("xmas".index(test[0]), test[1], int(test[2:])), goto))
        else:
            default = rule
    workflows.update({name : (tuple(rules), default)})

def dfs(name, lower, upper):
    if name == "R" or any(l > u for l, u in zip(lower, upper)):
        return 0
    if name == "A":
        return functools.reduce(operator.mul, [u-l+1 for l, u in zip(lower, upper)])

    res = 0
    rules, default = workflows[name]
    l, u = list(lower), list(upper)
    for test, goto in rules:
        pos, cmp, val = test
        if cmp == "<":
            res += dfs(goto, tuple(l), tuple(u[:pos] + [val-1] + u[pos+1:]))
            l[pos] = val
        else:
            res += dfs(goto, tuple(l[:pos] + [val+1] + l[pos+1:]), tuple(u))
            u[pos] = val
        
        if l[pos] > u[pos]: return res

    res += dfs(default, tuple(l), tuple(u))
    return res
            
print(dfs("in", tuple([1] * 4), tuple([4000] * 4)))
