import sys
import re

TIME = 1000

particles = []
for n, line in enumerate(sys.stdin.read().splitlines()):
    particles.append(list(map(lambda x : list(map(int, x.split(","))), re.findall("p=<(.+)>, v=<(.+)>, a=<(.+)>", line)[0])))

for t in range(TIME):
    for n, p in enumerate(particles):
        for d in range(3):
            p[1][d] += p[2][d]
            p[0][d] += p[1][d]

print(min((sum(map(abs, p[0])), n) for n, p in enumerate(particles))[1])
