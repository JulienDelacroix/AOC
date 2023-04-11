import sys
import statistics
import numpy as np

# We are searching for RP and RV, such that:
#     - at t1: RP + RV * t1 = p1 + s1 * t1
#     - at t2: RP + RV * t2 = p2 + s2 * t2
#     - at t3: RP + RV * t3 = p3 + s3 * t3
#     - ...
#
# For any p, v, t:
#   RP + RV * t = p + s * t => (p - RP) / (s - RS) = -t
#                           => (p[i] - RP[i]) / (s[i] - RS[i]) = -t for i in {0, 1, 2}
#
#   => (p[0] - RP[0]) * (s[1] - RS[1]) = (p[1] - RP[1]) * (s[0] - RS[0])
#   =>    s[1] * RP[0] 
#       - s[0] * RP[1] 
#       - p[1] * RS[0]
#       + p[0] * RS[1] 
#       = p[0] * s[1] - p[1] * s[0] + RP[0] * RS[1] - RP[1] * RS[0]  
#                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
#                                            not linear :-(
#    
# Consider (p1, v1) and (p2, v2) and substract to get rid of RP[0] * RS[1] - RP[1] * RS[0] terms
#   =>    (s2[1] - s1[1]) * RP[0] 
#       + (s1[0] - s2[0]) * RP[1]
#       + (p1[1] - p2[1]) * RS[0]
#       + (p2[0] - p1[0]) * RS[1]
#       = p2[0] * s2[1] - p2[1] * s2[0] - (p1[0] * s1[1] - p1[1] * s1[0])
#
# Now, this is a linear equation with 4 unknowns (RP[0], RP[1], RS[0], RS[1]) 
# ... so one can solve a linear system of 4 equations derived from 4 pairs of hailstones to find RP[0] and RP[1] 
# ... and repeat this procedure with (x, z) or (y, z) instead of(x, y) to find RP[2]

def fillLinearSystem(A, b, offset, p1, s1, p2, s2):
    p1 = tuple(v - offset for v in p1)
    p2 = tuple(v - offset for v in p2)
    A.append((s2[1] - s1[1], s1[0] - s2[0], p1[1] - p2[1], p2[0] - p1[0]))
    b.append(p2[0] * s2[1] - p2[1] * s2[0] - (p1[0] * s1[1] - p1[1] * s1[0]))


hailstones = []
for line in sys.stdin.read().splitlines():
    s1, s2 = line.split("@")
    pos = tuple(map(int, s1.split(",")))
    speed = tuple(map(int, s2.split(",")))
    hailstones.append((pos, speed))

# to cope with finite precision of numpy (float64), select hailstones with smaller (absolute) values and recenter
hailstones.sort(key = lambda h: max(abs(v) for v in h[0]))
offset = round(statistics.mean(v for h in hailstones[:5] for v in h[0]))

A_xy, b_xy = [], []
A_yz, b_yz = [], []
h1 = hailstones[0]
for h2 in hailstones[1:5]:
    fillLinearSystem(A_xy, b_xy, offset, h1[0][:2], h1[1][:2], h2[0][:2], h2[1][:2])
    fillLinearSystem(A_yz, b_yz, offset, h1[0][1:], h1[1][1:], h2[0][1:], h2[1][1:])

Px, Py, Vx, Vy = np.linalg.solve(A_xy, b_xy)
Py, Pz, Vy, Vz = np.linalg.solve(A_yz, b_yz)

print(round(Px) + round(Py) + round(Pz) + offset*3)
