import sys

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
card_strength = { c : list(reversed(cards)).index(c) for c in cards }

hands = []
for line in sys.stdin.read().splitlines():
    cards, value = line.split()

    if cards == "JJJJJ":
        hand_type = [(5)]
    else:
        hand_type = list(reversed(sorted(cards.count(c) for c in set(cards) if c != 'J')))
        hand_type[0] += cards.count('J')

    hand_strength = tuple(card_strength[c] for c in cards)
    hands.append(((hand_type, hand_strength), int(value)))

res = 0
for rank, h in enumerate(sorted(hands)):
    _, value = h
    res += ((rank+1) * value)
print(res)
