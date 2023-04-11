from collections import deque

left = deque()
right = deque(range(1, int(input())+1))

while len(right) > 1:
    while len(left) + 1 < len(right):
        left.append(right.popleft())
    right.popleft()
    right.append(left.popleft())

print(right[0])
