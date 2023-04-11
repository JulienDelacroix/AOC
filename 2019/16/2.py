import itertools

signal = [ int(c) for c in input() ] * 10000
offset = int("".join(map(str, signal[:7])))

# Important observations:  
#   - offset > len(signal) / 2
#   - when i > len(signal)/2: 
#       new_signal[i] = 0 * signal[0] + 0 * signal[1] + ... + 0 * signal[i-1] + 1 * signal[i] + 1 * signal[i+2] + ... + 1 * signal[len(signal)-1]
#                     = sum(signal[i:])

truncated_signal = signal[offset:]
for _ in range(100):
    truncated_signal = [abs(d) % 10 for d in reversed(list(itertools.accumulate(reversed(truncated_signal)))) ]

print("".join(str(i) for i in truncated_signal[0:8]))
