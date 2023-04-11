import itertools

def next_password(s):
    if s == "": return "a"
    if s[len(s)-1] == 'z': 
        return next_password(s[:-1]) + "a"
    else:
        return s[:-1] + chr(ord(s[len(s)-1]) + 1)

def valid(password):
    pair_offsets = [i for i in range(1, len(password)) if password[i] == password[i-1]]
    return (
        any(ord(password[i]) == (ord(password[i-1])+1) == (ord(password[i-2])+2) for i in range(2, len(password)))
        and not any(c in password for c in {'i', 'o', 'l'})
        and any((i+1 < j) for i, j in itertools.combinations(pair_offsets, 2))
    )

password = input()
while(not valid(password)):
    password = next_password(password)
print(password)
