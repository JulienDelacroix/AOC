import sys
from collections import Counter

tracker = Counter()
for line in sys.stdin.read().splitlines():
    tokens = line.split()
    if eval("tracker[\"" + tokens[4] +"\"] " + " ".join(tokens[5:])):
        tracker[tokens[0]] +=  (1 if tokens[1] == "inc" else -1) * int(tokens[2])

print(tracker.most_common()[0][1])
