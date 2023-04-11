import sys

keypad = [ "00100", "02340", "56789", "0ABC0", "00D00"]

x, y = 0, 2
for line in sys.stdin.read().splitlines():
    for c in line:
        if c == 'R' and x < 4 and keypad[y][x+1] != '0': x += 1
        if c == 'L' and x > 0 and keypad[y][x-1] != '0': x -= 1
        if c == 'U' and y > 0 and keypad[y-1][x] != '0': y -= 1
        if c == 'D' and y < 4 and keypad[y+1][x] != '0': y += 1
    print(keypad[y][x], end="")
print()