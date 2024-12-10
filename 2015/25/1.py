import sys
import re

target_row, target_col = map(int, re.findall(r"(\d+)", sys.stdin.read().splitlines()[0]))

row = col = index = 1
while row != target_row:
    index += (row + col) - 1
    row += 1
while col != target_col:
    index += (row + col)
    col += 1

print((20151125 * pow(252533, index - 1, 33554393)) % 33554393)
