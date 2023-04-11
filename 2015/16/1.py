import sys
import re

required = { "children" : 3, "cats" : 7, "samoyeds" : 2, "pomeranians" : 3, "akitas" : 0, "vizslas" : 0, "goldfish" : 5, "trees" : 3, "cars" : 2, "perfumes" : 1}

for index, line in enumerate(sys.stdin.read().splitlines()):
    attr = { attr.split(":")[0] : int(attr.split(":")[1]) for attr in re.findall(" (\w+: \d+)", line) }
    if all(k not in attr or attr[k] == v for k, v in required.items()):
        print(index+1)
        break
