import re
import sys

PARAM = r"(\d{1,3})"

res = 0
for x ,y in re.findall(re.escape("mul(%s,%s)") % (PARAM, PARAM), sys.stdin.read()):
    res += int(x) * int(y)
print(res)
