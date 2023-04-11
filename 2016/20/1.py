import sys
from queue import PriorityQueue

events = PriorityQueue()
for i, line in enumerate(sys.stdin.read().splitlines()):
    intervals = tuple(map(int, line.split("-")))
    events.put((intervals[0], (True, i)))
    events.put((intervals[1], (False, i)))

next_valid = 0
opened = set()
while not events.empty():
    ip, (open, index) = events.get()
    if open:
        if len(opened) == 0 and ip > next_valid:
            print(next_valid)
            break
        opened.add(index)
    else:
        opened.remove(index)
        if len(opened) == 0:
            next_valid = ip + 1
