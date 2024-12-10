import sys

def safe(seq):
    if seq != list(sorted(seq)) and seq != list(reversed(sorted(seq))):
        return False
    if not all(1 <= abs(v1 - v2) <= 3 for v1, v2 in zip(seq, seq[1:])):
        return False
    return True

def safe2(seq):
    return any(safe(seq[0:skipped] + seq[skipped+1:]) for skipped in range(len(seq)))
        
sequences = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]
print(sum(safe2(seq) for seq in sequences))
