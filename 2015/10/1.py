input = list(map(int, "3113322113"))

for _ in range(40):
    current = input[0]
    current_count = 0
    result = []    
    for c in input:
        if c == current:
            current_count += 1
        else:
            result.append(current_count)
            result.append(current)
            current = c
            current_count = 1
    result.append(current_count)
    result.append(current)
    input = result

print(len(result))
