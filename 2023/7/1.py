import sys

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_strength = { c : list(reversed(cards)).index(c) for c in cards }

hands = []
for line in sys.stdin.read().splitlines():
    cards, value = line.split()
    hand_type = tuple(reversed(sorted(cards.count(c) for c in set(cards))))
    hand_strength = tuple(card_strength[c] for c in cards)
    hands.append(((hand_type, hand_strength), int(value)))

res = 0
for rank, h in enumerate(sorted(hands)):
    _, value = h
    res += ((rank+1) * value)
print(res)
