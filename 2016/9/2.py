import re

def uncompress(compressed):
    result = 0
    i = 0
    while i < len(compressed):
        while i < len(compressed) and compressed[i] != '(':
            i += 1
            result += 1

        if i == len(compressed): break
        i += 1
        instruction = []
        while compressed[i] != ')':
            instruction.append(compressed[i])
            i += 1
        i += 1
        
        seq, times = map(int, re.findall("(\d+)x(\d+)", "".join(instruction))[0])
        result += times * uncompress(compressed[i:i+seq])
        i += seq
    return result

print(uncompress(input()))
