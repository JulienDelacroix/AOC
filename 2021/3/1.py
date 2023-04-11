import sys

lines = sys.stdin.read().splitlines()

gamma = epsilon = ""
for i in range(len(lines[0])):
    more1 = [v[i] for v in lines].count('1') > len(lines)/2
    gamma += ('1' if more1 else '0')
    epsilon += ('0' if more1 else '1')

print(int(gamma, 2) * int(epsilon, 2))
