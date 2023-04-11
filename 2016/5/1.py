import hashlib

secret = input()
res = []
i =  0
while len(res) < 8:
    hash = hashlib.md5((secret + str(i)).encode()).hexdigest()
    if hash[:5] == "00000":
        res.append(hash[5])
    i += 1
    
print("".join(res))
