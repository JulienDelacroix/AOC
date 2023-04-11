import sys

#############
#01.2.3.4.56#
###A#B#C#D###
  #A#B#C#D#
  #########

hallway = [-1] * 7
hallway_x = [1, 2, 4, 6, 8, 10, 11]

rooms = [ [] for _ in range(4) ]
rooms_x = [3, 5, 7, 9]

amphipod_cost = [1, 10, 100, 1000]

hallway_to_rooms = [
    [ [1], [1, 2], [1, 2, 3], [1, 2, 3, 4] ],
    [ [], [2], [2, 3], [2, 3, 4] ],
    [ [], [], [3], [3, 4] ],
    [ [2], [], [], [4] ],
    [ [3, 2], [3], [], [] ],
    [ [4, 3, 2], [4, 3], [4], [] ],
    [ [5, 4, 3, 2], [5, 4, 3], [5, 4], [5] ]
]

tracker = {}
def dfs(hallway, rooms, cost_so_far):

    key = "".join("ABCD"[h] if h != -1 else '.' for h in hallway) + "|".join("".join("ABCD"[c] for c in r) for r in rooms)
    if key in tracker and tracker[key] <= cost_so_far: 
        return None
    tracker[key] = cost_so_far

    if all(r == ([i] * 2) for i, r in enumerate(rooms)):
        return cost_so_far
    
    best_cost = None

    # move from hallway to rooms
    for h, amphipod in enumerate(hallway):
        if amphipod != -1 and all(val == amphipod for val in rooms[amphipod]):
            path = hallway_to_rooms[h][amphipod]
            if all(hallway[p] == -1 for p in path):
                move_cost = amphipod_cost[amphipod] * (abs(rooms_x[amphipod] - hallway_x[h]) + (2 - len(rooms[amphipod])))
                hallway[h] = -1
                rooms[amphipod].append(amphipod)

                total_cost = dfs(hallway, rooms, cost_so_far + move_cost)
                if total_cost and (not best_cost or total_cost < best_cost):
                    best_cost = total_cost
                
                hallway[h] = rooms[amphipod].pop()

    # move from rooms to hallway
    for r, room in enumerate(rooms):
        if len(room) and not all(v == r for v in room):
            for h in range(7):
                path = hallway_to_rooms[h][r]
                if hallway[h] == -1 and all(hallway[pos] == -1 for pos in path):
                    amphipod = room.pop()
                    hallway[h] = amphipod
                    move_cost = amphipod_cost[amphipod] * (abs(rooms_x[r] - hallway_x[h]) + (2 - (len(room))))

                    total_cost = dfs(hallway, rooms, cost_so_far + move_cost)
                    if total_cost and (not best_cost or total_cost < best_cost):
                        best_cost = total_cost

                    room.append(hallway[h])
                    hallway[h] = -1
    return best_cost    

for line in reversed(sys.stdin.read().splitlines()):
        amphipods = [c for c in line if c.isalpha()]
        for index, c in enumerate(amphipods):
            rooms[index].append("ABCD".index(c))

print(dfs(hallway, rooms, 0))
