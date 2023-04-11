data = input()

while len(data) < 35651584:
    data = data + "0" + "".join(['1' if c == '0' else '0' for c in reversed(data) ])
data = data[:35651584]

while len(data) % 2 == 0:
    data = "".join('1' if data[i] == data[i+1] else '0' for i in range(0, len(data)-1, 2))

print(data)
