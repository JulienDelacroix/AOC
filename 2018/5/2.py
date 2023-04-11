polymer = input()
units = set(c.lower() for c in polymer)

def reduce(u):
    stack = []
    for c in polymer:
        if c == u or c == u.swapcase(): continue
        stack.append(c)
        while len(stack) > 1 and stack[-2].swapcase() == stack[-1]:
            stack.pop()
            stack.pop()
    return len(stack)

print(min(reduce(u) for u in units))
    