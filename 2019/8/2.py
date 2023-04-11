from collections import defaultdict

H, W = 6, 25

def groupBy(iterable, blocksize):
    args = [iter(iterable)] * blocksize
    return zip(*args)

picture = defaultdict(lambda : '2')
for layer in groupBy(input(), H * W):
    for y in range(H):
        for x in range(W):
            if picture[(x, y)] == '2':
                picture[(x, y)] = layer[y * W  + x]

for y in range(H):
    for x in range(W):
        match picture[(x, y)]:
            case '0': print(' ', end="")
            case '1': print('#', end="")
            case '2': print('?', end="")
    print()
