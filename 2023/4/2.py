import sys
import re
from collections import Counter

res = 0
tracker = Counter()
for line in sys.stdin.read().splitlines():
    id_str, winning_str, card_str = re.findall("Card +(\d+): ([^|]+) \| (.+)", line)[0]
    id = int(id_str)
    winning = set(map(int, re.findall("(\d+)", winning_str)))
    card = map(int, re.findall("(\d+)", card_str))
    
    tracker[id] += 1
    score = sum(1 for n in card if n in winning)
    if score :
        for newCard in range(id + 1, id + 1 + score):
            tracker[newCard] += tracker[id]

print(sum(tracker.values()))
