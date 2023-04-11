import sys
import re

screen = set()
for line in sys.stdin.read().splitlines():
    if line.startswith("rect"):
        xmax, ymax = map(int, re.findall("rect (\d+)x(\d+)", line)[0])
        for x in range(xmax):
            for y in range(ymax):
                screen.add((x, y))
        
    elif line.startswith("rotate column"):
        col, shift = map(int, re.findall("rotate column x=(\d+) by (\d+)", line)[0])
        removed = set((col, row) for row in range(6) if (col, row) in screen and (col, (row + 6 - shift) % 6) not in screen)
        added = set((col, row) for row in range(6) if (col, row) not in screen and (col, (row + 6 - shift) % 6) in screen)
        screen -= removed
        screen |= added

    elif line.startswith("rotate row"):
        row, shift = map(int, re.findall("rotate row y=(\d+) by (\d+)", line)[0])
        removed = set((col, row) for col in range(50) if (col, row) in screen and ((col + 50 - shift) % 50, row) not in screen)
        added = set((col, row) for col in range(50) if (col, row) not in screen and ((col + 50 - shift) % 50, row) in screen)
        screen -= removed
        screen |= added

print(len(screen))
