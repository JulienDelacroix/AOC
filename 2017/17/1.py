from collections import deque

STEP = 345

spinlock = deque()
for i in range(2017+1):
    spinlock.rotate(-STEP - 1)
    spinlock.appendleft(i)

print(spinlock[1])
