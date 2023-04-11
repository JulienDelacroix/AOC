import sys

a = int(sys.stdin.readline().split()[-1])
b = int(sys.stdin.readline().split()[-1])

res = 0
for _ in range(5000000):
    while True:
        a = (a *16807) % 2147483647
        if a % 4 == 0 : break
    
    while True:
        b = (b *48271) % 2147483647
        if b % 8 == 0: break

    if bin(a)[-16:] == bin(b)[-16:]:
        res += 1
print(res)
