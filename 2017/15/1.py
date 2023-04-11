import sys

a = int(sys.stdin.readline().split()[-1])
b = int(sys.stdin.readline().split()[-1])

res = 0
for _ in range(40000000):
    a = (a *16807) % 2147483647
    b = (b *48271) % 2147483647
    if bin(a)[-16:] == bin(b)[-16:]:
        res += 1
print(res)
