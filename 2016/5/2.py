import hashlib

secret = input()
res = ['_'] * 8
i =  0
while '_' in res:
    hash = hashlib.md5((secret + str(i)).encode()).hexdigest()
    if hash[:5] == "00000":
        if '0' <= hash[5] < '8':
            pos = ord(hash[5]) - ord('0')
            if res[pos] == '_':
                res[pos] = hash[6]
                print("\r" + "".join(res), end="", flush=True)
    i += 1
print()
    