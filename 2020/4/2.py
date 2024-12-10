import sys
import re

mandatory = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" }

def check(data):
    field, value = data
    match(field):
        case "byr": return 1920 <= int(value) <= 2002
        case "iyr": return 2010 <= int(value) <= 2020
        case "eyr": return 2020 <= int(value) <= 2030
        case "hgt": return (value[-2:] == "cm" and 150 <= int(value[:-2]) <= 193) or (value[-2:] == "in" and 59 <= int(value[:-2]) <= 76)
        case "hcl": return re.fullmatch(r"#[0-9a-f]{6}", value)
        case "ecl": return re.fullmatch(r"amb|blu|brn|gry|grn|hzl|oth", value)
        case "pid": return re.fullmatch(r"[0-9]{9}", value)
    
res = 0
for block in list(sys.stdin.read().split("\n\n")):
    data = dict()
    for line in block.splitlines():
        for field, value in re.findall(r"(%s)\:(\S+)" % "|".join(mandatory), line):
            data.update({field : value})
    res += (len(data) == len(mandatory) and all(check(d) for d in data.items()))
print(res)
