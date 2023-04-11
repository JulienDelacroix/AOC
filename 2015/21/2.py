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

rings_combos = list(itertools.combinations([(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)], 2))

boss = tuple(int(re.findall("\d+", line)[0]) for line in sys.stdin.read().splitlines())
max_cost = 0
for weapon in [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]:
    for armor in [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]:
        for rings in rings_combos:
            equiped_player = (100, weapon[1] + sum(r[1] for r in rings), armor[2] + sum(r[2] for r in rings))
            cost =  weapon[0] + armor[0] + sum(r[0] for r in rings)
        
            if f(equiped_player, boss) == 1:
                max_cost = max(max_cost, cost)

print(max_cost)
