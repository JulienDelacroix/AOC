from collections import deque

elves = deque(range(1, int(input())+1))
while len(elves) > 1:
    elves.rotate(-1)
    elves.popleft()

print(elves[0])
