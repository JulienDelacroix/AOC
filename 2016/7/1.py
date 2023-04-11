import sys
import re

res = 0
for line in sys.stdin.read().splitlines():
    abba = [False, False]
    for index, seq in enumerate(re.findall("(\w+)", line)):
        abba[(index % 2)] |= any((seq[i] != seq[i+1] and seq[i] == seq[i+3] and seq[i+1] == seq[i+2]) for i in range(len(seq)-3))
    if abba[0] and not abba[1]:
        res += 1

print(res)
