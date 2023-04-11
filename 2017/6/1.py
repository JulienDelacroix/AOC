tracker = set()
bins = list(map(int, input().split()))
tracker.add(tuple(bins))

step = 0
while True:
    items = max(bins)
    b = bins.index(items)
    bins[b] = 0
    for i in range(items):
        bins[(b + 1 + i) % len(bins)] += 1
    step += 1
    if tuple(bins) in tracker:
        break
    tracker.add(tuple(bins))
    
print(step)
