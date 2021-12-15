data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]

cave = []
for ln in data:
    cave.append([int(x) for x in ln])
H = len(cave)
W = len(cave[0])

deltas = [(0,-1), (0,1), (1,0), (-1,0)]
def valid(pos):
    return 0 <= pos[0] < W and 0 <= pos[1] < H

def findPath(pos):
    # dijkstra's algorithm
    x = []
    visited = {}
    
    x.append((cave[0][0], pos))

    path = {}
    cost = {}

    cost[pos] = 0

    while x:
        # get min element
        item = x[0]

        for d in x:
            if d[0] < item[0]:
                item = d
        x.remove(item)

        cur = item[1]

        if cur == (H-1, W-1): return path
        
        visited[cur] = 1
        for d in deltas:
            new_pos = (cur[0] + d[0], cur[1] + d[1])
            if not valid(new_pos) or new_pos in visited: continue

            weight = cave[new_pos[1]][new_pos[0]]
            newCost = cost[cur] + weight
            cost_ = cost[new_pos] if new_pos in cost else 1000000
            if cost_ > newCost:
                x.append((newCost,new_pos))
                cost[new_pos] = newCost
                path[new_pos] = cur

    return path

path = findPath((0,0))
pos = (W-1,H-1)
cost = 0 
while pos != (0,0):
    cost += cave[pos[1]][pos[0]]
    cave[pos[1]][pos[0]] = -1
    pos = path[pos]
print(cost)

