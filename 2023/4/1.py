import sys
import re

res = 0
for line in sys.stdin.read().splitlines():
    winning_str, card_str = re.findall(r"Card +\d+: ([^|]+) \| (.+)", line)[0]
    winning = set(map(int, re.findall(r"(\d+)", winning_str)))
    card = map(int, re.findall(r"(\d+)", card_str))

    score = sum(1 for n in card if n in winning)
    res += 2 ** (score - 1) if score else 0

print(res)
