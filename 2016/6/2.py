import sys
from collections import Counter

lines = sys.stdin.read().splitlines()
cols = list(zip(*lines))
print("".join(Counter(c).most_common()[-1][0] for c in cols))
