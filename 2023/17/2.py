import sys
import queue

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : int(c)})

xmax = max(p[0] for p in grid.keys())
ymax = max(p[1] for p in grid.keys())
goal = (xmax, ymax)

# A* search
def h(pos):
    return abs(goal[0] - pos[0]) + abs(goal[1] - pos[1])

q = queue.PriorityQueue()
costs = {}

start_pos = (0, 0)
start_state = (start_pos, True, True)
q.put((h(start_pos), 0, start_state))
costs.update({start_state : 0})

while not q.empty():
    _, currentCost, state = q.get()
    currentPos, horizontal, vertical = state
    if currentPos == goal: 
        print(currentCost)
        break

    currentX, currentY = currentPos
    for sign in (-1, 1):
        if horizontal:
            for nextX in range(currentX + 4*sign, currentX + 11*sign, sign):
                nextPos = (nextX, currentY)
                if nextPos in grid:
                    nextCost = currentCost + sum(grid[(x, currentY)] for x in range(currentX + sign, nextX + sign, sign))
                    nextState = (nextPos, False, True)
                    if nextState not in costs or nextCost < costs[nextState]:
                        costs.update({nextState : nextCost})
                        q.put((nextCost + h(nextPos), nextCost, nextState))

        if vertical:
            for nextY in range(currentY + 4*sign, currentY + 11*sign, sign):
                nextPos = (currentX, nextY)
                if nextPos in grid:
                    nextCost = currentCost + sum(grid[(currentX, y)] for y in range(currentY + sign, nextY + sign, sign))
                    nextState = (nextPos, True, False)
                    if nextState not in costs or nextCost < costs[nextState]:
                        costs.update({nextState : nextCost})
                        q.put((nextCost + h(nextPos), nextCost, nextState))

