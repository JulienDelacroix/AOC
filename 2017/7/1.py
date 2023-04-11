import sys

programs = set()
referenced = set() 
for line in sys.stdin.read().splitlines():
    tokens = line.split(" -> ")
    programs.add(tokens[0].split()[0])
    if len(tokens) > 1:
        referenced.update(tokens[1].split(", "))
print(programs - referenced)
