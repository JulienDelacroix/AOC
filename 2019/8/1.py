H, W = 6, 25

def groupBy(iterable, blocksize):
    args = [iter(iterable)] * blocksize
    return zip(*args)

res = (H * W, 0)
for layer in groupBy(input(), H * W):
    res = min(res, (layer.count('0'), layer.count('1') * layer.count('2')))

print(res[1])
