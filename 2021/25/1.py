import sys

def update(moving, fixed, nextpos):
    moved = set(pos for pos in moving if nextpos(pos) not in fixed)
    moving -= moved
    moving.update(nextpos(pos) for pos in moved)
    return len(moved)

lines = sys.stdin.read().splitlines()
xmax, ymax = len(lines[0]), len(lines)

right, down = set(), set()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != '.':
            (right if c == '>' else down).add((x, y))

for step in range(1, 1000):
    moved_right = update(right, right | down, lambda pos: ((pos[0] + 1) % xmax, pos[1]))
    moved_down = update(down, right | down, lambda pos: (pos[0], (pos[1] + 1) % ymax))

    if moved_right == 0 and moved_down == 0:
        print(step)
        break
