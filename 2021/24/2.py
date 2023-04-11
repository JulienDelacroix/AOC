import sys
import re
import functools

pattern = """\
inp w
mul x 0
add x z
mod x 26
div z (-?\d+)
add x (-?\d+)
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y (-?\d+)
mul y x
add z y
"""
params = [list(map(int, p)) for p in re.findall(pattern, "".join(sys.stdin.readlines()))]

def monad(z, w, p):
    x = z % 26 + p[1]
    z = z // p[0]
    if (x != w):
        z *= 26
        z += (w + p[2])
    return z

@functools.lru_cache(None)
def dfs(depth, z):
    if depth == 14:
        return [] if z == 0 else None

    remaining_reducing_steps = sum(p[1]<0 for p in params[depth:]) + 1
    if z > 26 ** remaining_reducing_steps: return None

    for digit in range(1, 10):
        next_z = monad(z, digit, params[depth])
        next_digits = dfs(depth+1, next_z)
        if next_digits is not None: 
            return [digit] + next_digits
    return None

digits = dfs(0, 0)
print("".join(str(d) for d in digits))
