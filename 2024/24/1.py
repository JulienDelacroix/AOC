import sys
import re
import itertools
import funtools

from collections import Counter
from queue import Queue


# grid
grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : c})

# blocks
blocks = list(sys.stdin.read().split("\n\n"))
lines = blocks[0].splitlines()

# lines
for line in sys.stdin.read().splitlines():
    # reading tuple
    winning_str, card_str = re.findall(r"Card +\d+: ([^|]+) \| (.+)", line)[0]
    # reading int list
    winning = set(map(int, re.findall(r"(\d+)", line)))
    


# cycle handling
step = 0
remaining = 1000000000
visited = {}
while remaining:
    [...]
    step += 1
    remaining -= 1
    key = [...]
    if key not in visited:
        visited.update({key : step})
    else:
        cycle_len = step - visited[key]
        remaining = remaining % cycle_len



from urllib.request import Request, urlopen
import os.path

def get_input(year, day):
    input_file_name = f'advent input {year}-{day}.txt'
    if os.path.exists(input_file_name):
        with open(input_file_name, 'r') as input_file:
            return input_file.read()
        
    try:
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        request = Request(url, headers={'cookie': 'session=get_your_value_from_your_browser_by_looking_at_the_request_header'})
        input_bytes = urlopen(request).read()
        input_text = input_bytes.decode('utf-8')
        with open(input_file_name, 'w') as input_file:
            input_file.write(input_text)
        return input_text
    except Exception as e:
        print(e)
        return None


for y in range(min(p[1] for p in pannels.keys()), max(p[1] for p in pannels.keys())+1):
    for x in range(min(p[0] for p in pannels.keys()), max(p[0] for p in pannels.keys())+1):
        print('#' if pannels[(x, y)] == 1 else ' ', end="")
    print()
