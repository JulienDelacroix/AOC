s = input()
print(sum((ord(c1) - ord('0')) for c1, c2 in zip(s, s[1 :] + s[: 1]) if c1 == c2))
