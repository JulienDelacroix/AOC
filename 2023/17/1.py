import sys
import queue

grid = {}
for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        grid.update({(x, y) : int(c)})

xmax = max(p[0] for p in grid.keys())
ymax = max(p[1] for p in grid.keys())
goal = (xmax, ymax)

openset = queue.PriorityQueue()
costs = {}

start_state = ((0, 0), True, True)
openset.put((0, start_state))
costs.update({start_state : 0})

res = 1000000
while not openset.empty():
    currentCost, state = openset.get()
    currentPos, horizontal, vertical = state
    if currentPos == goal: 
        res = min(res, currentCost)
        continue

    currentX, currentY = currentPos
    for sign in (-1, 1):
        if horizontal:
            for nextX in range(currentX + sign, currentX + 4*sign, sign):
                nextPos = (nextX, currentY)
                if nextPos in grid:
                    nextCost = currentCost + sum(grid[(x, currentY)] for x in range(currentX + sign, nextX + sign, sign))
                    nextState = (nextPos, False, True)
                    if nextState not in costs or nextCost < costs[nextState]:
                        costs.update({nextState : nextCost})
                        openset.put((nextCost, nextState))

        if vertical:
            for nextY in range(currentY + sign, currentY + 4*sign, sign):
                nextPos = (currentX, nextY)
                if nextPos in grid:
                    nextCost = currentCost + sum(grid[(currentX, y)] for y in range(currentY + sign, nextY + sign, sign))
                    nextState = (nextPos, True, False)
                    if nextState not in costs or nextCost < costs[nextState]:
                        costs.update({nextState : nextCost})
                        openset.put((nextCost, nextState))

print(res)
