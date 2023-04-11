s = input()
print(sum((ord(c1) - ord('0')) for c1, c2 in zip(s, s[len(s) // 2 :] + s[: len(s) // 2]) if c1 == c2))
