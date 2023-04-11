bins = list(map(int, input().split()))
tracker = { tuple(bins) : 0 }

step = 0
while True:
    items = max(bins)
    b = bins.index(items)
    bins[b] = 0
    for i in range(items):
        bins[(b + 1 + i) % len(bins)] += 1
    step += 1
    if tuple(bins) in tracker:
        print(step - tracker[tuple(bins)])
        break
    tracker.update({tuple(bins) : step})
