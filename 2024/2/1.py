import sys

def safe(seq):
    if seq != list(sorted(seq)) and seq != list(reversed(sorted(seq))):
        return False
    if not all(1 <= abs(v1 - v2) <= 3 for v1, v2 in zip(seq, seq[1:])):
        return False
    return True

sequences = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]
print(sum(safe(seq) for seq in sequences))
