stack = []
for c in input():
    stack.append(c)
    while len(stack) > 1 and stack[-2].swapcase() == stack[-1]:
        stack.pop()
        stack.pop()

print(len(stack))
    