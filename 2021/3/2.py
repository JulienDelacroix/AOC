import sys

lines = sys.stdin.read().splitlines()

oxygen = co2 = lines
for  i in range(len(lines[0])):
    if len(oxygen) > 1:
        mode_o = '1' if [v[i] for v in oxygen].count('1') >= len(oxygen)/2 else '0'
        oxygen = [v for v in oxygen if v[i] == mode_o]
    if len(co2) > 1:
        mode_c = '1' if [v[i] for v in co2].count('1') >= len(co2)/2 else '0'
        co2 = [v for v in co2 if v[i] != mode_c]

print(int(oxygen[0], 2) * int(co2[0], 2))