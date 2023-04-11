offsets = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir = x = y = 0
for command in input().split(", "):
    if command[0] == 'R': dir = (dir + 1) % 4
    if command[0] == 'L': dir = (dir - 1) % 4

    distance = int(command[1:])
    x, y = x + offsets[dir][0] * distance, y + offsets[dir][1] * distance

print(abs(x) + abs(y))