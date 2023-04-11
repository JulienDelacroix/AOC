import sys
from collections import Counter

template_block, insertion_block = sys.stdin.read().split("\n\n")
template = template_block.splitlines()[0]

letter_tracker = Counter(template)
pair_tracker = Counter(zip(template, template[1:]))

for _ in range(40):
    pair_udpates = Counter()
    for line in insertion_block.splitlines():
        pair, inserted = line.split(" -> ")

        pair_count = pair_tracker[(pair[0], pair[1])]
        pair_udpates[(pair[0], pair[1])] -= pair_count
        pair_udpates[(pair[0], inserted)] += pair_count
        pair_udpates[(inserted, pair[1])] += pair_count
        letter_tracker[inserted] += pair_count

    for pair, delta in pair_udpates.items():
        pair_tracker[pair] += delta

sorted_by_freq = letter_tracker.most_common()
print(sorted_by_freq[0][1] - sorted_by_freq[-1][1])
