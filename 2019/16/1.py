signal = [ int(c) for c in input() ]
print("".join(map(str, signal[:7])))

for phase in range(100):
    new_signal = []
    for position in range(len(signal)):
        new_signal.append(abs(sum(i * [0, 1, 0, -1][((n+1) // (position+1) ) % 4] for n, i in enumerate(signal))) % 10)
    signal = new_signal

print("".join(map(str, signal[:8])))
    