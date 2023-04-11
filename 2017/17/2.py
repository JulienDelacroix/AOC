from collections import deque

STEP = 345

after_zero = None
spinlock = deque()
for i in range(50000000+1):
    spinlock.rotate(-STEP - 1)
    spinlock.appendleft(i)
    if spinlock[-1] == 0:
        after_zero = i

print(after_zero)
