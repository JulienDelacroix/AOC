import sys
import re
import numpy as np

ITER=18

def transform(a):
    for k in range(4):
        r = np.rot90(a, k=k, axes=(1, 0))
        yield r
        yield np.flipud(r)

rules = {}
for line in sys.stdin.read().splitlines():
    pattern_str, enhanced_str = re.findall("(.+) => (.+)", line)[0]
    pattern = np.array([ [(1 if c == '#' else 0) for c in row] for row in pattern_str.split("/") ])
    enhanced = np.array([ [(1 if c == '#' else 0) for c in row] for row in enhanced_str.split("/") ])
    for p in transform(pattern):
        rules.update({ tuple(map(tuple, p)) : enhanced })

pattern = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
for _ in range(ITER):
    subCount = len(pattern) / (3 if len(pattern) % 2 else 2)
    subPatterns = [ np.hsplit(row, subCount) for row in np.vsplit(pattern, subCount) ]
    subEnhanced = [ [ rules[tuple(map(tuple, p))] for p in row ] for row in subPatterns ]
    pattern = np.concatenate([np.concatenate(row, axis=1) for row in subEnhanced], axis=0)

print(np.sum(pattern))
