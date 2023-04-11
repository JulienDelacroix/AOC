import sys

x = y = 1
for line in sys.stdin.read().splitlines():
    for c in line:
        if c == 'R' and x < 2: x += 1
        if c == 'L' and x > 0: x -= 1
        if c == 'U' and y > 0: y -= 1
        if c == 'D' and y < 2: y += 1                        
    print(y*3+x+1, end="")
print()