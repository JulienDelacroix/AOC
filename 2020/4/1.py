import sys
import re

mandatory = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" } #, "cid" }

res = 0
for block in list(sys.stdin.read().split("\n\n")):
    data = set()
    for line in block.splitlines():
        data |= set(re.findall(r"(%s)\:\S+" % "|".join(mandatory), line))
    res += (len(data) == len(mandatory))
print(res)        
