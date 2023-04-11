import functools

def n4(pos):
    x, y = pos
    for ox, oy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        if (0 <= (x + ox) < 128) and (0 <= (y + oy) < 128):
            yield (x + ox, y + oy)

def knot(s): 
    numbers = list(range(256))
    N = len(numbers)
    pos = skip = 0

    sequences = list(map(ord, s)) + [17, 31, 73, 47, 23]
    for _ in range(64):
        for v in sequences:
            for i in range(v // 2):
                n1 = (pos + i) % N
                n2 = (pos + v - 1 - i) % N
                numbers[n1], numbers[n2] = numbers[n2], numbers[n1]
            pos = (pos + v + skip) % N
            skip += 1

    xorlist = [ functools.reduce(lambda r, v : r ^ v, numbers[i * 16 : i* 16 + 16], 0) for i in range(16) ]    
    return "".join(bin(v)[2:].zfill(8) for v in xorlist)

seed = input()
squares = set()
for y in range(128):
    for x, bit in enumerate(knot(seed + "-" + str(y))):
        if bit == '1':
            squares.add((x, y))

res = 0
visited = set()
for x in range(128):
    for y in range(128):
        start = (x, y)
        if start not in squares or start in visited: continue
        res += 1
        q = [start]
        visited.add(start)
        while len(q):
            pos = q.pop()
            for npos in n4(pos):
                if npos in squares and npos not in visited:
                    q.append(npos)
                    visited.add(npos)

print(res)
