import sys

res = 0
for block in list(sys.stdin.read().split("\n\n")):
    answers = set()
    for line in block.splitlines():
        answers |= set(line)
    res += len(answers)
    print(answers)
print(res)
