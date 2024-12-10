import sys
import re

required = { "children" : 3, "cats" : 7, "samoyeds" : 2, "pomeranians" : 3, "akitas" : 0, "vizslas" : 0, "goldfish" : 5, "trees" : 3, "cars" : 2, "perfumes" : 1}

def match(k, value , required):
    if k == "cats" or k == "trees":
        return (value > required)
    if k == "pomeranians" or k == "goldfish":
        return (value < required)
    return (value == required)

for index, line in enumerate(sys.stdin.read().splitlines()):
    attr = { attr.split(":")[0] : int(attr.split(":")[1]) for attr in re.findall(r" (\w+: \d+)", line) }
    if all(k not in attr or match(k, attr[k], v) for k, v in required.items()):
        print(index+1)
        break
