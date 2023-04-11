x = y = 0
visited = set()
visited.add((x, y))
for command in input():
    if command == '>': x += 1
    elif command == '<': x -= 1
    elif command == '^': y -= 1
    elif command == 'v': y += 1
    visited.add((x, y))
print(len(visited))
