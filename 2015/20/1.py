target = int(input())

def simulate(N):
    presents = [ 0 ] * N
    for start in range(1, N):
        pos = start
        while pos < N:
            presents[pos] += 10 * start
            pos += start
    return enumerate(presents)

for index, presents in simulate(1000000):
    if presents >= target:
        break
print(index)
