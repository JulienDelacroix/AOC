target = int(input())

def simulate(N):
    presents = [ 0 ] * N
    for start in range(1, N):
        pos = start
        for _ in range(50):
            presents[pos] += 11 * start
            pos += start
            if pos >= N: break
    return enumerate(presents)

for index, presents in simulate(1000000):
    if presents >= target:
        break
print(index)
