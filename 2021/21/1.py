import sys

def roll3():
    dice = 0
    while True:
        yield (3 * dice + 3) % 100 + 3
        dice += 3

pos = []
scores = [0, 0]
for line in sys.stdin.read().splitlines():
    pos.append(int(line.split()[4]))

r = p = 0
roll = roll3()
while scores[1-p] < 1000:
    pos[p] = (pos[p] - 1 + next(roll)) % 10 + 1
    scores[p] += pos[p]
    r += 1
    p = 1 - p

print(3 * r * min(scores))
