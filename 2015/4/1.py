import hashlib

secret = input()
for i in range(10000000):
    if hashlib.md5((secret + str(i)).encode()).hexdigest()[:5] == "00000":
        break
print(i)
