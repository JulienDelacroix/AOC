import sys
import re

sum = 0
for line in sys.stdin.read().splitlines():
    red = max(map(int, re.findall(r"(\d+) red,?", line)))
    green = max(map(int, re.findall(r"(\d+) green,?", line)))
    blue = max(map(int, re.findall(r"(\d+) blue,?", line)))
    sum += (red * green * blue)
print(sum)
