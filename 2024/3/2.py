import re
import sys

PARAM = r"(\d{1,3})"
DO = "do()"
DONT = "don't()"

enabled = True
res = 0
for instr, x , y in re.findall(
    r"(%s|%s|%s)" % (
        re.escape("mul(%s,%s)") % (PARAM, PARAM),
        re.escape(DO),
        re.escape(DONT)
    ),
    sys.stdin.read()
):
    if instr == DO:
        enabled = True
    elif instr == DONT:
        enabled = False
    elif enabled:
        res += int(x) * int(y)
print(res)
