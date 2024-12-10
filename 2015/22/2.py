import sys
import re

boss_inital_hp, boss_damage = map(int, (re.findall(r"\d+", line)[0] for line in sys.stdin.read().splitlines()))
min_mana = 100000

def dfs(turn, player_hp, shield_timer, poison_timer, recharge_timer, mana, spent_mana, boss_hp):
    global min_mana

    if turn == 0: player_hp -= 1
    if player_hp <= 0 or (turn == 0 and mana < 53) or spent_mana >= min_mana: return
    if boss_hp <= 0:
        min_mana = min(min_mana, spent_mana)
        return

    a = 0
    if shield_timer > 0:
        a = 7
        shield_timer -= 1
    if poison_timer > 0:
        boss_hp -= 3
        poison_timer -= 1
    if recharge_timer > 0:
        mana += 101
        recharge_timer -= 1    
    
    if turn == 0:
        if mana >= 53:
            dfs(1, player_hp, shield_timer, poison_timer, recharge_timer, mana - 53, spent_mana + 53, boss_hp - 4)

        if mana >= 73:
            dfs(1, player_hp + 2, shield_timer, poison_timer, recharge_timer, mana - 73, spent_mana + 73, boss_hp - 2)

        if mana >= 113 and shield_timer == 0:
            dfs(1, player_hp, 6, poison_timer, recharge_timer, mana - 113, spent_mana + 113, boss_hp)

        if mana >= 173 and poison_timer == 0:
            dfs(1, player_hp, shield_timer, 6, recharge_timer, mana - 173, spent_mana + 173, boss_hp)

        if mana >= 229 and recharge_timer == 0:
            dfs(1, player_hp, shield_timer, poison_timer, 5, mana - 229, spent_mana + 229, boss_hp)

    else:
        dfs(0, player_hp - max(1, boss_damage - a), shield_timer, poison_timer, recharge_timer, mana, spent_mana, boss_hp)

dfs(0, 50, 0, 0, 0, 500, 0, boss_inital_hp)
print(min_mana)
