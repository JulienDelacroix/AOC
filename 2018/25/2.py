# grid
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        break

# blocks
blocks = list(sys.stdin.read().split("\n\n"))
lines = blocks[0].splitlines()

# lines
for line in sys.stdin.read().splitlines():
    # reading tuple
    winning_str, card_str = re.findall(r"Card +\d+: ([^|]+) \| (.+)", line)[0]
    # reading int list
    winning = set(map(int, re.findall(r"(\d+)", line)))
    