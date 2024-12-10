import math

# using chinese remainder theorem
def solve(a_vec, n_vec):
    N = math.prod(n_vec)
    return sum(a * pow(N // n, -1, n) * N // n for a, n in zip(a_vec, n_vec)) % N

time = int(input())
all_bus = list((int(id), index) for index, id in enumerate(input().split(",")) if id != "x")
all_ids = [id for id, _ in all_bus]

print(solve([id - index for id, index in all_bus], all_ids))
