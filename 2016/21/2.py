import sys
import itertools

commands = sys.stdin.read().splitlines()
s = [c for c in "abcdefgh"]

for original in itertools.permutations((c for c in "abcdefgh"), 8):
    s = original
    for command in commands:
        tokens = command.split()
        if command.startswith("swap position"):
            i1, i2 = int(tokens[2]), int(tokens[5])
            s[i1], s[i2] = s[i2], s[i1]
        elif command.startswith("swap letter"):
            c1, c2 = tokens[2], tokens[5]
            s = [c1 if c == c2 else (c2 if c == c1 else c)  for c in s]
        elif command.startswith("rotate left"):
            n = int(tokens[2]) % len(s)
            s = s[n:] + s[:n]
        elif command.startswith("rotate right"):
            n = int(tokens[2]) % len(s)
            s = s[-n:] + s[:-n]
        elif command.startswith("reverse positions"):
            i1, i2 = int(tokens[2]), int(tokens[4])
            s = s[0:i1] + list(reversed(s[i1:i2+1])) + s[i2+1:]
        elif command.startswith("move position"):
            i1, i2 = int(tokens[2]), int(tokens[5])
            v = s.pop(i1)
            s.insert(i2, v)
        elif command.startswith("rotate based"):
            c = tokens[6]
            i = s.index(c)
            n = (1 + i + (1 if i >= 4 else 0)) % len(s)
            s = s[-n:] + s[:-n]
    
    if "".join(s) == "fbgdceah":
        break

print("".join(original))
