import sys
import re

state = re.findall("Begin in state (\w).", sys.stdin.readline())[0]
steps = int(re.findall("Perform a diagnostic checksum after (\d+) steps.", sys.stdin.readline())[0])

input = "".join(sys.stdin.readlines())
pattern = """\
In state (\w+):
  If the current value is 0:
    - Write the value (\d).
    - Move one slot to the (\w+).
    - Continue with state (\w).
  If the current value is 1:
    - Write the value (\d).
    - Move one slot to the (\w+).
    - Continue with state (\w).
"""
rules = {}
for s, v1, dir1, ns1, v2, dir2, ns2  in re.findall(pattern, input):
    rules.update({s : ((int(v1), 1 if dir1 == "right" else -1, ns1), (int(v2), 1 if dir2 == "right" else -1, ns2))})

ones = set()
pos = 0
for _ in range(steps):
    if pos in ones:
        v, offset, state = rules[state][1]
        if v == 0:
            ones.remove(pos)
    else:
        v, offset, state = rules[state][0]
        if v == 1:
            ones.add(pos)
    pos += offset

print(len(ones))
