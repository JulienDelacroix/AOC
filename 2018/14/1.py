INPUT = int("084601")

recipes = [3, 7]
c0, c1 = 0, 1

while(len(recipes) < INPUT + 10):
    recipes.extend(map(int, str(recipes[c0] + recipes[c1])))
    c0 = (c0 + recipes[c0] + 1) % len(recipes)
    c1 = (c1 + recipes[c1] + 1) % len(recipes)

print("".join(map(str, recipes[INPUT:])))
