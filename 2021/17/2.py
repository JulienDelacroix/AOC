import re
x1, x2, y1, y2 = map(int, re.findall(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", input())[0])

res = 0
for init_vx in range(x2+1):
    if ((init_vx * (init_vx+1)) // 2) < x1: continue # cannot reach
    for init_vy in range(y1-1, 100):
        ymax = x = y = 0
        vx = init_vx
        vy = init_vy
        while True:
            x += vx 
            y += vy
            vx = max(0, vx-1)
            vy -= 1
            if x1 <= x <= x2 and y1 <= y <= y2:
                res += 1
                break #found

            if x > x2: break #overshoot
            if vy < 0 and y < y1: break # went through
print(res)