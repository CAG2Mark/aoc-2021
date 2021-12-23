from copy import deepcopy
from collections import defaultdict
import heapq as heap

data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

burrow0 = []
burrow1 = []
burrow2 = []
burrow3 = []


hallway = [-1]*11

d = {"A": 0, "B": 1, "C": 2, "D": 3}
d_ = {0: "A", 1: "B", 2: "C", 3: "D"}

energy = {0: 1, 1: 10, 2: 100, 3: 1000}
hallwaypos = {0: 0, 1: 1, 2: 3, 3: 5, 4: 7, 5: 9, 6: 10}
burrowpos = {0: 2, 1: 4, 2: 6, 3: 8}
burrowpos_rev = {2: 0, 4: 1, 6: 2, 8: 3}

burrow0.append(d[data[3][3]])
burrow0.append(3)
burrow0.append(3)
burrow0.append(d[data[2][3]])

burrow1.append(d[data[3][5]])
burrow1.append(1)
burrow1.append(2)
burrow1.append(d[data[2][5]])

burrow2.append(d[data[3][7]])
burrow2.append(0)
burrow2.append(1)
burrow2.append(d[data[2][7]])

burrow3.append(d[data[3][9]])
burrow3.append(2)
burrow3.append(0)
burrow3.append(d[data[2][9]])

# testing
testing = False
if testing:
    burrow0 = [0]
    burrow1 = [1,1]
    burrow2 = [2,2]
    burrow3 = [3,3]
    hallway = [-1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1]

burrows = [burrow0, burrow1, burrow2, burrow3]
def is_complete(burrows):
    for i, b in enumerate(burrows):
        if len(b) != 4: return False
        for a in b:
            if a != i: return False
    return True

def can_move(pos1, pos2, hallway):
    blocked = False
    for p in range(min(pos1, pos2), max(pos1, pos2)+1):
        if hallway[p] != -1:
            blocked = True
            break
    if blocked: return False
    return True

def get_moves(burrows, hallway):
    possibilities = []
    for i in range(len(hallway)):

        if i in burrowpos_rev:
            pos = burrowpos_rev[i]
            burrow = burrows[burrowpos_rev[i]]
            # if empty, ignore
            if not burrow: continue
            # if burrow is partially or fully complete, ignre
            flag = False
            for b in burrow:
                if b != pos:
                    flag = True
                    break
            if not flag: continue

            if len(burrow) > 4: 
                print("Error: burrow length > 4")
                return
        if i not in burrowpos_rev and hallway[i] == -1: continue

        for j in range(len(hallway)):
            if i == j: continue
            # if already filled, just an optimisation
            if hallway[j] != -1: continue
            # if og pos already in hallway can't move to a non-burrow position
            if not i in burrowpos_rev and not j in burrowpos_rev: continue

            # if destination is above brrow and is full, ignore
            if j in burrowpos_rev and len(burrows[burrowpos_rev[j]]) >= 4: continue
            
            # check all positions between cur spot and next spot
            next_pos = i
            # if is not in burrow, don't include current pos in the checking range
            if not i in burrowpos_rev:
                if j > i: next_pos += 1
                else: next_pos -= 1

            if not can_move(next_pos, j, hallway): continue
            bur = deepcopy(burrows)

            hallw = deepcopy(hallway)
            temp = 0

            dist = abs(j-i)

            # take from current position
            if i in burrowpos_rev:
                burpos = burrowpos_rev[i]
                temp = bur[burpos].pop()
                dist += 4 - len(bur[burpos])
            else:
                temp = hallw[i]
                hallw[i] = -1
            # move to next position
            if j in burrowpos_rev:
                burpos = burrowpos_rev[j]
                dist += 4 - len(bur[burpos])
                if burpos != temp: continue
                flag = False
                
                for b in bur[burpos]:
                    if b != temp: 
                        flag = True
                        break
                if flag: continue

                if len(bur[burpos]) >= 4: continue
                bur[burpos].append(temp)

            else:
                hallw[j] = temp
            cost = energy[temp]
            cost *= dist

            possibilities.append((cost, (bur, hallw)))

    return possibilities

def dijkstra(burrows, hallway, visited = []):
    visited = visited.copy()
    visited.append(str((burrows, hallway)))
    
    costs = defaultdict(lambda: float('inf'))
    costs[str((burrows, hallway))] = 0
    parents = {}

    pq = []
    heap.heappush(pq, (0, (burrows, hallway)))

    while pq:
        cost, node = heap.heappop(pq)
        visited.append(str(node))
        # print()
        # print(str(node), cost)
        # print("->")
        if is_complete(node[0]):
            print(costs[str(node)])
            return costs, parents, str(node)
        poss = get_moves(node[0], node[1])
        for weight, p in poss:
            if str(p) in visited: continue
            new_cost = costs[str(node)] + weight
            # print(p, "cost:", new_cost, "\t increase:", weight) 
            if costs[str(p)] > new_cost:
                parents[str(p)] = str(node)
                costs[str(p)] = new_cost
                heap.heappush(pq, (new_cost, p))

    return costs, parents, ""


costs, parents, last = dijkstra(burrows, hallway)
path = [last]
while last != str((burrows, hallway)):
    last = parents[last]
    path.insert(0, last)

import ast
for p in path:
    a = ast.literal_eval(p)
    for h in a[1]:
        print("." if h == -1 else d_[h], end="")
    print()
    print("##", end = "")
    for b in a[0]:
        if len(b) < 4: print(".#", end="")
        else: print(d_[b[3]], end="#")
    print("#")
    print("##", end="")
    for b in a[0]:
        if len(b) < 3: print(".#", end="")
        else: print(d_[b[2]], end="#")
    print("#")
    print("##", end="")
    for b in a[0]:
        if len(b) < 2: print(".#", end="")
        else: print(d_[b[1]], end="#")
    print("#")
    print("##", end="")
    for b in a[0]:
        if len(b) < 1: print(".#", end="")
        else: print(d_[b[0]], end="#")
    print("#")
    print("total cost", costs[p])

