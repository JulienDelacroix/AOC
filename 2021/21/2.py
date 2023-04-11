import sys
import functools

roll_freq = { 3 : 1, 4 : 3, 5 : 6, 6 : 7, 7 : 6, 8 : 3, 9: 1}

@functools.lru_cache(None)
def dfs(player, pos1, pos2, score1, score2, count):
    if score2 >= 21:
        return (count, 0) if player else (0, count)

    total_w1 = total_w2 = 0
    for roll, freq in roll_freq.items():
        new_pos1 = (pos1 - 1 + roll) % 10 + 1
        new_score1 = score1 + new_pos1

        w1, w2 = dfs(1-player, pos2, new_pos1, score2, new_score1, count * freq)
        total_w1 += w1
        total_w2 += w2
    return (total_w1, total_w2)

pos = []
scores = [0, 0]
for line in sys.stdin.read().splitlines():
    pos.append(int(line.split()[4]))

print(max(dfs(0, *pos, *scores, 1)))
