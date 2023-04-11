trap_patterns = ("^^.", ".^^", "^..", "..^")
row = input()

res = 0
for _ in range(400000):
    res += row.count('.')
    completed = "." + row + '.'
    row = "".join('^' if completed[i:i+3] in trap_patterns else '.' for i in range(len(row)))

print(res)
