import math

time = int(input())
all_ids = list(int(id) for id in input().split(",") if id != "x")

print(math.prod(min((id - time % id, id) for id in all_ids)))
