import sys

xpos = depth = aim = 0
for line in sys.stdin.read().splitlines():
    dir, val = line.split()
    if dir == "forward": 
        xpos += int(val)
        depth += aim * int(val)
    if dir == "down": aim += int(val)
    if dir == "up": aim -= int(val)

print(xpos * depth)
