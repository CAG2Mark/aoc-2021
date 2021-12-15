import heapq as heap

data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]

H_ = len(data)
W_ = len(data[0])
cave = []
for i in range(5*H_):
    temp = []
    for j in range(5*W_):
        val = (i//H_ + j//W_ + int(data[i%H_][j%W_]))
        if val > 9: val %= 9
        temp.append(val)
    cave.append(temp)

H = len(cave)
W = len(cave[0])

deltas = [(0,-1), (0,1), (1,0), (-1,0)]
def valid(pos):
    return 0 <= pos[0] < W and 0 <= pos[1] < H

def findPath(pos):
    # dijkstra's algorithm
    x = []
    visited = {}
    
    heap.heappush(x,(cave[0][0], pos))

    path = {}
    cost = {}

    cost[pos] = 0

    while x:
        # get min element
        item = heap.heappop(x)

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
                heap.heappush(x,(newCost,new_pos))
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

# for ln in cave:
#    print(''.join(['.' if x == -1 else str(x) for x in ln]))
