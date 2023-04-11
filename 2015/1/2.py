line = input()
print(min(i for i in range(len(line)) if line[:i].count('(') < line[:i].count(')')))

