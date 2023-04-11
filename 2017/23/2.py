b_start = 84 * 100 + 100000
c = b_start + 17000
h = 0
for b in range(b_start, c+1, 17):
	for d in range(2, b):
		if b % d == 0:
			h += 1
			break
print(h)
