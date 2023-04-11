import string
from collections import deque

LEN = 16
letters = deque(string.ascii_lowercase[0:LEN])
dance = input().split(",")

step = 0
remaining = 1000000000
visited = {}
while remaining:
    for instr in dance:
        if instr.startswith("s"):
            letters.rotate(int(instr[1:]))

        if instr.startswith("x"):
            pos1, pos2 = map(int, instr[1:].split("/"))
            letters[pos1], letters[pos2] = letters[pos2], letters[pos1]

        if instr.startswith("p"):
            pos1, pos2 = map(lambda v : letters.index(v), instr[1:].split("/"))
            letters[pos1], letters[pos2] = letters[pos2], letters[pos1]

    step += 1
    remaining -= 1
    key = tuple(letters)
    if key not in visited:
        visited.update({key : step})
    else:
        cycle_len = step - visited[key]
        remaining = remaining % cycle_len

print("".join(letters))
    


