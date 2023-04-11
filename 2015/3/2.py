x = [0, 0]
y = [0, 0]
visited = set()
visited.add((0, 0))
for step, command in enumerate(input()):
    if command == '>': x[step % 2] += 1
    elif command == '<': x[step % 2] -= 1
    elif command == '^': y[step % 2] -= 1
    elif command == 'v': y[step % 2] += 1
    visited.add((x[step % 2], y[step % 2]))
print(len(visited))
