from queue import Queue

seed = int(input())

def n4(pos):
    x, y = pos
    for ox, oy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        if (x + ox) >= 0 and (y + oy) >= 0:
            yield (x + ox, y + oy)

def wall(pos):
    x, y = pos
    return bin(x * x + 3 * x + 2 * x * y + y + y * y + seed)[2:].count('1') % 2 == 1

q = Queue()
q.put(((1, 1), 0))
visited = {(1, 1)}

while not q.empty():
    pos, d = q.get()
    if pos == (31, 39):
        print(d)
        break
    for npos in n4(pos):
        if npos not in visited and not wall(npos):
            q.put((npos, d+1))
            visited.add(npos)
