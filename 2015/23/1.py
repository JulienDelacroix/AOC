def collatz(n):
    if n == 1: return 0
    if n % 2 == 0:
        return 1 + collatz(n // 2)
    else:
        return 1 + collatz(3 * n + 1)

a = 1
a *= 3
a += 1
a *= 3
a += 1
a *= 9
a += 2
a *= 9
a += 2
a *= 3
a += 2
a *= 3
print(collatz(a))
