INPUT = list(map(int, "084601"))

L = len(INPUT)

recipes = [3, 7]
c0, c1 = 0, 1

while recipes[-L:] != INPUT and recipes[-L-1:-1] != INPUT:
    recipes.extend(map(int, str(recipes[c0] + recipes[c1])))
    c0 = (c0 + recipes[c0] + 1) % len(recipes)
    c1 = (c1 + recipes[c1] + 1) % len(recipes)

print(len(recipes) - L - (0 if recipes[-L:] == INPUT else 1))
