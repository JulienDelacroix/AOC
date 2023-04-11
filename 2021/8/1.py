import sys
counters = [0] * 10

for line in sys.stdin.read().splitlines():
    pattern_list, output_list = line.split("|")
    for token in output_list.strip().split(" "):
        counters[len(token)] += 1

print(counters[2] + counters[3] + counters[4] + counters[7])
