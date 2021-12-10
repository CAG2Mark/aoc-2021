data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
hmap = []
for x in data:
    hmap.append([int(c) for c in x])
lows = []

hsize = len(hmap[0])
vsize = len(hmap)
for y, row in enumerate(hmap):
    for x, col in enumerate(row):
        if y != 0 and hmap[y-1][x] <= col: continue
        if y != len(hmap)-1 and hmap[y+1][x] <= col: continue
        if x != 0 and hmap[y][x-1] <= col: continue
        if x != len(row)-1 and hmap[y][x+1] <= col: continue
        lows.append((x,y))
def bfs(pos):
    visited = []
    basin = []
    stack = []
    stack.append(pos)
    while stack:
        # get smallest
        smallest = 10
        smallestindex = 0
        for i,p in enumerate(stack):
            if hmap[p[1]][p[0]] < smallest:
                smallest = hmap[p[1]][p[0]]
                smallestindex = i
        cur_pos = stack.pop(smallestindex)
        x = cur_pos[0]
        y = cur_pos[1]
        cur = hmap[y][x]
        visited.append(cur_pos)
        buf=[]
        truth = []
        if y != 0 and not (x,y-1) in basin:
            truth.append(hmap[y-1][x] >= cur)
            buf.append((x,y-1))

        if y != vsize-1 and not (x,y+1) in basin:
            truth.append(hmap[y+1][x] >= cur)
            buf.append((x,y+1))

        if x != 0 and not (x-1,y) in basin:
            truth.append(hmap[y][x-1] >= cur)
            buf.append((x-1,y))

        if x != hsize-1 and not (x+1,y) in basin: 
            truth.append(hmap[y][x+1] >= cur)
            buf.append((x+1,y))

        if sum(truth) == len(truth) and cur != 9:
            if not cur_pos in basin: basin.append(cur_pos)
            for b in buf:
                if not b in visited: stack.append(b)
    return len(basin)

basins = []
for l in lows:
    basins.append(bfs(l))
basins.sort()
basins = basins[-1:-4:-1]
prod = 1
for b in basins: prod *= b
print(prod)
