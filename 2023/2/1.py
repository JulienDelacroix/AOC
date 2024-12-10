import sys
import re

sum = 0
for line in sys.stdin.read().splitlines():
    id = int(re.findall(r"Game (\d+):", line)[0])
    red = max(map(int, re.findall(r"(\d+) red,?", line)))
    green = max(map(int, re.findall(r"(\d+) green,?", line)))
    blue = max(map(int, re.findall(r"(\d+) blue,?", line)))
    if (red <= 12 and green <= 13 and blue <=14):
        sum += id
print(sum)
