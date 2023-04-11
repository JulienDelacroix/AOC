import sys

xpos = depth = 0
for line in sys.stdin.read().splitlines():
    dir, val = line.split()
    if dir == "forward": xpos += int(val)
    if dir == "down": depth += int(val)
    if dir == "up": depth -= int(val)

print(xpos * depth)
