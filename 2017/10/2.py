import functools
numbers = list(range(256))
N = len(numbers)
pos = skip = 0
sequences = list(map(ord, input())) + [17, 31, 73, 47, 23]
print(sequences)

for _ in range(64):
    for v in sequences:
        for i in range(v // 2):
            n1 = (pos + i) % N
            n2 = (pos + v - 1 - i) % N
            numbers[n1], numbers[n2] = numbers[n2], numbers[n1]
        pos = (pos + v + skip) % N
        skip += 1
        print(pos, v, numbers)

print(numbers)
h = 0
for i in range(16):
    print(hex(functools.reduce(lambda r, v : r ^ v, numbers[i * 16 : i* 16 + 16], 0))[2:], end="")
print()
