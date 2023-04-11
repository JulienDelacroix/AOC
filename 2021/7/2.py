import sys

crabs_pos = list(map(int, input().split(",")))
crabs_counters = [0] * (max(crabs_pos)+1)
for p in crabs_pos:
    crabs_counters[p] += 1

cumulated_cost_left = []
current_count = current_cost = cumulated_cost = 0
for c in crabs_counters:
    current_cost += current_count
    cumulated_cost += current_cost
    current_count += c
    cumulated_cost_left.append(cumulated_cost)

cumulated_cost_right = []
current_count = current_cost = cumulated_cost = 0 
for c in reversed(crabs_counters):
    current_cost += current_count
    cumulated_cost += current_cost    
    current_count += c
    cumulated_cost_right.append(cumulated_cost)
cumulated_cost_right.reverse()

print(min(cumulated_cost_left[v] + cumulated_cost_right[v] for v in range(len(crabs_counters))))
