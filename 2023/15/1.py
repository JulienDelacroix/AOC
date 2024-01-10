import sys

res = 0
for word in sys.stdin.read().splitlines()[0].split(","):
    h = 0
    for c in word:
        h += ord(c)
        h *= 17
        h %= 256
    res += h
print(res)
