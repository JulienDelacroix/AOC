import sys
import re
from collections import Counter

res = 0
for line in sys.stdin.read().splitlines():
    name, sector, checksum = re.findall(r"(.*)-(\d+)\[(.*)\]", line)[0]
    counter = Counter(c for c in sorted(name) if c != '-')
    if checksum == "".join(v for v, _ in counter.most_common(5)):
        res += int(sector)
        deciphered = "".join(' ' if c == '-' else chr(ord('a') + (ord(c) - ord('a') + int(sector)) % 26) for c in name)
        if "northpole" in deciphered:
            print(sector)
            exit(0)
