import re
from collections import deque

P, M = map(int, re.findall("(\d+)", input()))

scores = [0] * P
p = 0
q = deque()
for m in range(0, M):
    if m != 0 and m % 23 == 0:
        q.rotate(7)
        scores[p] += m + q.popleft()
    else:
        q.rotate(-2)
        q.appendleft(m)
    p = (p + 1) % P

print(max(scores))
