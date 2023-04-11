import hashlib
from collections import Counter

salt = input()

def hash(i):
    return hashlib.md5((salt + str(i)).encode()).hexdigest()

def triples(h):
    return next((h[c] for c in range(len(h) - 2) if h[c] == h[c+1] == h[c+2]), None)

def fives(h):
    return set(h[c] for c in range(len(h) - 4) if h[c] == h[c+1] == h[c+2] == h[c+3] == h[c+4])

count5 = Counter()
for i in range(1000):
    for c in fives(hash(i)):
        count5[c] += 1

found = 0
for i in range(30000):
    for c in fives(hash(i)):
        count5[c] -= 1
    for c in fives(hash(i+1000)):
        count5[c] += 1
    
    t = triples(hash(i))
    if t is not None and count5[t]:
        found += 1
        if found == 64:
            print(i)
            break
