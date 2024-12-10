import sys
import re
import itertools

def f(p0, p1):
    hp0, damage0, armor0 = p0
    hp1, damage1, armor1 = p1
    while True:
        hp1 -= (damage0 - armor1)
        if hp1 <= 0:
            return 0    
        hp0 -= (damage1 - armor0)
        if hp0 <= 0:
            return 1

rings_combos = []
for n in range(0, 4):
    rings_combos.extend(itertools.combinations([(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)], n))

boss = tuple(int(re.findall(r"\d+", line)[0]) for line in sys.stdin.read().splitlines())
min_cost = 1000
for weapon in [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]:
    for armor in [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]:
        for rings in rings_combos:
            equiped_player = (100, weapon[1] + sum(r[1] for r in rings), armor[2] + sum(r[2] for r in rings))
            cost =  weapon[0] + armor[0] + sum(r[0] for r in rings)
        
            if f(equiped_player, boss) == 0:
                min_cost = min(min_cost, cost)

print(min_cost)
