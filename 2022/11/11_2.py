import sys
import re
import math
from collections import Counter

tracker = Counter()

MOD = 1
monkeys = []
for desc in sys.stdin.read().split("\n\n"):
    lines = desc.splitlines()
    id = int(re.findall(r"\d+", lines[0])[0])
    items = list(map(int, re.findall(r"\d+", lines[1])))
    operation = re.findall(r"Operation: new = (.*)", lines[2])[0]
    test = int(re.findall(r"\d+", lines[3])[0])
    test_true = int(re.findall(r"\d+", lines[4])[0])
    test_false = int(re.findall(r"\d+", lines[5])[0])
    monkeys.append([id, items, operation, test, test_true, test_false])
    MOD *= test

for i in range(10000):
    for m in monkeys:
        for old in m[1]:
            tracker[m[0]] += 1
            next_val = eval(m[2]) % MOD
            next_m = m[4] if next_val % m[3] == 0 else m[5]
            (monkeys[next_m])[1].append(next_val)
        m[1].clear()

sorted_counters = sorted(tracker.values())
print(sorted_counters[-1]*sorted_counters[-2])
