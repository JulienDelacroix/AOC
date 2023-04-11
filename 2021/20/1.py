import sys

def n9(pos):
    x, y = pos
    for next_pos in [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]:
        yield next_pos

def state(pos, infinite_pixels):
    res = 0
    for p in n9(pos):
        res *= 2
        res += 1 if (p in pixels or (infinite_pixels and p not in arround_pixels)) else 0
    return algo_block[res] == "#" 
    
algo_block, input_block = sys.stdin.read().split("\n\n")
algo = algo_block.splitlines()[0]

pixels = set()
arround_pixels = set()

for y, line in enumerate(input_block.splitlines()):
    for x, c in enumerate(line): 
        if c == "#":
            pixels.add((x, y))
            arround_pixels.update(n9((x, y)))

for step in range(2):
    new_arround_pixels = set()
    for p in pixels:
        for p2 in n9(p):
            new_arround_pixels.update(n9(p2))
    
    new_pixels = set()    
    for p in new_arround_pixels: 
        if state(p, algo[0] == "#" and step % 2 == 1) : new_pixels.add(p)
    
    pixels = new_pixels
    arround_pixels = new_arround_pixels

print(len(pixels))
