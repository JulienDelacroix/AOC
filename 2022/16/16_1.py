import sys
import re

def FloydWarshallAPSP(m):
    dist = { source : { dest : 1000000 for dest in m } for source in m}
  
    for k in m.keys():
        dist[k][k] = 0
        for v in m[k]:
            dist[k][v] = 1

    for k in m.keys():
        for i in m.keys():
            for j in m.keys():
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def dfs(time, pos, valves, total_pressure):
    if time <= 0: return total_pressure

    best = total_pressure
    for next_pos in valves:
        if (DIST[pos][next_pos] < time) and PRESSURE[next_pos]:
            next_time = time - DIST[pos][next_pos] - 1
            best = max(best, dfs(next_time, next_pos, valves - frozenset([next_pos]), total_pressure + PRESSURE[next_pos] * next_time))
    return best

VALVES = ["AA"]
PRESSURE = {}
tunnels = {}
for line in sys.stdin.read().splitlines():
    valve, rate, next_list = re.findall(r"Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)", line)[0]
    if int(rate) > 0:
        VALVES.append(valve)
    tunnels[valve] = next_list.split(", ")
    PRESSURE[valve] = int(rate)

dist = FloydWarshallAPSP(tunnels)
PRESSURE = [ PRESSURE[v] for v in VALVES ]
DIST = [ [ dist[source][dest] for source in VALVES ] for dest in VALVES ]


