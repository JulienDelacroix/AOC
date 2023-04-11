import sys
import math

reactions = {}
for line in sys.stdin.read().splitlines():
    in_list, out = line.split(" => ")
    out_count, out_type = out.split(" ")
    reactions.update({out_type : (int(out_count), [])})
    
    for in_item in in_list.split(", "):
        in_count, in_type = in_item.split(" ")
        reactions[out_type][1].append((int(in_count), in_type))


def compute_ore(fuel):
    inventory = { k : 0 for k in reactions.keys() }
    inventory["ORE"] = 0
    inventory["FUEL"] = -fuel

    while any(count < 0 and chemical != "ORE" for chemical, count in inventory.items()):
        for chemical, count in inventory.items():
            if chemical != "ORE" and count  < 0:
                out_count, in_list = reactions[chemical]
                repeat = math.ceil(-count / out_count)
                
                inventory[chemical] += repeat * out_count
                for in_count, in_type in in_list:
                    inventory[in_type] -= repeat * in_count
    return -inventory["ORE"]


low, high = 0, 1000000000000
while low <= high:
    mid = low + (high - low) // 2
    ore = compute_ore(mid)
    if ore < 1000000000000:
        low = mid + 1
    elif ore > 1000000000000:
        high = mid - 1

print(low-1)
