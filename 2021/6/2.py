import sys

timers = [0] * 10
for f in map(int, input().split(",")):
    timers[f] += 1

for _ in range(256):
    expired = timers[0]
    timers = timers[1:] + [0]
    timers[6] += expired
    timers[8] += expired
print(sum(timers))
