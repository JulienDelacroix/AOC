import sys
mappings = {"one" : "1", "two" : "2", "three" : "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine" : "9" }

sum = 0
for line in sys.stdin.read().splitlines():
    charlist = []
    for i in range(len(line)):
        if line[i].isdigit():
            charlist.append(line[i])
        for k, v in mappings.items():
            if line[i:].startswith(k):
                charlist.append(v)
    sum += int("".join([charlist[0], charlist[-1]]))
print(sum)
