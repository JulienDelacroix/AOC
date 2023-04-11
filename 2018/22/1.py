import re
import functools

@functools.lru_cache(None)
def erosion(x, y):
    if x == target_x and y == target_y: return  depth % 20183 
    if y == 0: return ((x * 16807) + depth) % 20183
    if x == 0: return ((y * 48271) + depth) % 20183
    return ((erosion(x-1, y) * erosion(x, y-1)) + depth ) % 20183

depth = int(re.findall("(\d+)", input())[0])
target_x, target_y = tuple(map(int, re.findall("(\d+)", input())))

print(sum(erosion(x, y) % 3 for x in range(0, target_x+1) for y in range(0, target_y+1)))
