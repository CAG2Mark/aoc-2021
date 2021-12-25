data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

grid = []
d = {".": 0, ">": 1, "v": 2}
for ln in data:
    grid.append([d[x] for x in ln])

def state():
    s = ""
    for ln in grid:
        s += "".join([str(i) for i in ln])
        s += "\n"
    return s

H = len(grid)
W = len(grid[0])

old_state = state()

cnt = 0
while True:
    old_state = state()
    # print(old_state)
    # print()

    # advance
    newgrid = []
    for i in range(H):
        newgrid.append([0]*W)

    # advance east
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == 0: continue
            elif col == 1 and not row[(x+1)%W]:
                newgrid[y][(x+1)%W] = 1
            else: 
                newgrid[y][x] = col

    grid = newgrid
    newgrid = []
    for i in range(H):
        newgrid.append([0]*W)
    
    # advance south
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == 0: continue
            if col == 2 and not grid[(y+1)%H][x]:
                newgrid[(y+1)%H][x] = 2
            else:
                newgrid[y][x] = col
    cnt += 1
    grid = newgrid
    new_state = state()
    # print(new_state)
    if new_state == old_state:
        print(cnt)
        break

        
