import hashlib
from queue import Queue

salt = input()

def hash(path):
    return hashlib.md5((salt + path).encode()).hexdigest()

q = Queue()
q.put(((0, 0), ""))

while not q.empty():
    pos, path = q.get()
    x, y = pos
    if x == 3 and y == 3:
        break

    opened = [c in "bcdef" for c in hash(path)[:4]]
    for m, (ox, oy) in enumerate([(0, -1), (0, 1), (-1, 0), (1, 0)]):
        if not opened[m]: continue
        npos = (x + ox, y + oy)
        if (0 <= npos[0] < 4) and (0 <= npos[1] < 4):
            q.put((npos, path + "UDLR"[m]))
    
print(path)
