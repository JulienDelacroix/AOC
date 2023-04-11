import sys
import re

ingredients = []
for line in sys.stdin.read().splitlines():
    ingredients.append(tuple(map(int, re.findall("(-?\d+)", line))))

def dfs(capacity, durability, flavor, texture, calories, index, teaspoons):
    i = ingredients[index]
    if index == len(ingredients) - 1:
        if calories + teaspoons * i[4] == 500:
            return (max(0, capacity + teaspoons * i[0])) * max(0, (durability + teaspoons * i[1])) * max(0, (flavor + teaspoons * i[2])) * max(0, (texture + teaspoons * i[3]))
        else:
            return 0
    else:
        return max(dfs(capacity + t * i[0], durability + t * i[1], flavor + t * i[2], texture + t * i[3], calories + t * i[4], index + 1, teaspoons - t) for t in range(0, teaspoons+1))

print(dfs(0, 0, 0, 0, 0, 0, 100))
