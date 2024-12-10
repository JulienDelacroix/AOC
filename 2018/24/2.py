import  sys
import re
from dataclasses import dataclass

@dataclass
class UnitGroup:
    team: str
    index: int
    units: int
    hp: int
    weak_to: set
    immune_to: set
    attack: int
    damage_type: str
    init: int

def damage(attacker, target):
    if attacker.damage_type in target.immune_to: return 0
    if attacker.damage_type in target.weak_to: return 2 * attacker.units * attacker.attack
    return attacker.units * attacker.attack

def sim(input, boost):
    groups = []
    for team, block in enumerate(input.split("\n\n")):
        lines = block.splitlines()
        team = lines[0].split(":")[0]
        for index, line in enumerate(lines[1:]):
            units, hp, attr, attack, damage_type, init = re.findall(r"(\d+) units? each with (\d+) hit points?(.*)with an attack that does (\d+) (\w+) damage at initiative (\w+)", line)[0]
            weak_to = immune_to = []
            for token in attr.strip(" )(").split("; "):
                if token.startswith("weak to"):
                    weak_to = token[8:].split(", ")
                elif token.startswith("immune to"):
                    immune_to = token[10:].split(", ")

            boosted_attack = int(attack) + (boost if team == "Immune System" else 0)
            groups.append(UnitGroup(team, index+1, int(units), int(hp), set(weak_to), set(immune_to), boosted_attack, damage_type, int(init)))

    while len(set(g.team for g in groups)) == 2:
        # selection phase
        pairs = []
        assigned = set()
        for attacker in reversed(sorted(groups, key=lambda g: (g.units * g.attack, g.init))):
            potential_targets = [t for t in groups if (t.team, t.index) not in assigned and t.team != attacker.team]
            if len(potential_targets):
                target = max(potential_targets, key=lambda t: (damage(attacker, t), t.units * t.attack, t.init))
                if damage(attacker, target) > 0:
                    assigned.add((target.team, target.index))
                    pairs.append((attacker, target))

        # attack phase
        total_killed = 0                    
        for attacker, target in reversed(sorted(pairs, key=lambda p : p[0].init)):
            if attacker.units <= 0 : continue
            killed = damage(attacker, target) // target.hp
            target.units -= killed
            total_killed += killed

        if total_killed  == 0: break
        groups = [g for g in groups if g.units >0]

    if set(g.team for g in groups) == { "Immune System" }:
        print(sum(g.units for g in groups))
        return True
    return False


input = sys.stdin.read()
for boost in range(10000):
    if sim(input, boost):
        break
