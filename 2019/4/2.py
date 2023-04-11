start, end = map(int, input().split("-"))

def valid(s):
    return all(c1 <= c2 for c1, c2 in zip(s, s[1:])) and any(s.count(c) == 2 for c in s)

print(sum(valid(str(n)) for n in range(start, end)))
