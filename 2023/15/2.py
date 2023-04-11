import sys

boxes = [[] for _ in range(256)]
focal = {}
for word in sys.stdin.read().splitlines()[0].split(","):
    h = 0
    for c in word:
        if c == '-':
            if word[:-1] in boxes[h]:
                boxes[h].remove(word[:-1])
            break
        elif c == '=':
            if word[:-2] not in boxes[h]:
                boxes[h].append(word[:-2])
            focal.update({word[:-2] : int(word[-1])})
            break
        else:
            h += ord(c)
            h *= 17
            h %= 256

res = 0
for b, items in enumerate(boxes):
    res += sum((b+1) * (s+1) * focal[len] for s, len in enumerate(items))
print(res)
