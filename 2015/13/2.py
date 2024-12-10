import sys
import re
import functools

hapiness = {}

@functools.lru_cache(None)
def dfs(first, last, remaining):
    if len(remaining) == 0:
        return hapiness[(last, first)] + hapiness[(first, last)]

    return max(
        ((hapiness[(last, person)] + (hapiness[(person, last)]) if last else 0)
        + dfs(first if first else person, person, remaining - {person}) for person in remaining)
    )

all_persons = set()
for line in sys.stdin.read().splitlines():
    person, gain_or_loose, units, neighbor = re.findall(r"(.*) would (gain|lose) (\d+) happiness units by sitting next to (.*)\.", line)[0]
    hapiness.update({(person, neighbor) : int(units) if gain_or_loose == "gain" else -int(units)})
    all_persons.add(person)

for person in all_persons:
    hapiness.update({(person, "myself") : 0, ("myself", person) : 0})
print(dfs(None, None, frozenset(all_persons) | {"myself"}))
