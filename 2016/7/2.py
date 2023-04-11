import sys
import re

res = 0
for line in sys.stdin.read().splitlines():
    aba = [set(), set()]
    for index, seq in enumerate(re.findall("(\w+)", line)):
        aba[(index % 2)].update([(seq[i], seq[i+1]) for i in range(len(seq)-2) if (seq[i] != seq[i+1] and seq[i] == seq[i+2])])

    matching = aba[0] & set((v2, v1) for (v1, v2) in aba[1])
    if len(matching):
        res += 1

print(res)
