numbers = list(range(256))
N = len(numbers)

pos = skip = 0
for v in map(int, input().split(",")):
    for i in range(v // 2):
        n1 = (pos + i) % N
        n2 = (pos + v - 1 - i) % N
        numbers[n1], numbers[n2] = numbers[n2], numbers[n1]
    pos = (pos + v + skip) % N
    skip += 1

print(numbers[0] * numbers[1])
