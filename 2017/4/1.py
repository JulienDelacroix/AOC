import  sys
from collections import Counter

res = 0
for line in sys.stdin.read().splitlines():
    res += (Counter(line.split()).most_common()[0][1] == 1)
print(res)

