data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]

power = []
for ln in data:
    power.append([int(c) for c in ln])

flashes = 0

N = 100

H = len(power)
W = len(power[0])
toInc = []
def valid(pos):
    return not ( pos[0] < 0 or pos[0] >= W or pos[1] < 0 or pos[1] >= H )

flashed = []

def getFlash():
    L = []
    for y,row in enumerate(power):
        for x,col in enumerate(row):
            if col >= 10 and not (x,y) in flashed: 
                flashed.append((x,y))
                L.append((x,y))
    return L

for _ in range(N):
    for y,row in enumerate(power):
        for x, col in enumerate(row):
            power[y][x] += 1
            if power[y][x] >= 10: power[y][x] = 10
    
    L = getFlash()
    while L:
        for pos in L:
            x = pos[0]
            y = pos[1]
            for y_ in range(pos[1]-1, pos[1]+2):
                for x_ in range(pos[0]-1, pos[0]+2):
                    if not valid((x_, y_)) or (y_ == y and x_ == x): continue
                    power[y_][x_] += 1
                    if power[y_][x_] >= 10:
                        power[y_][x_] = 10

        L = getFlash()

    for pos in flashed:
        power[pos[1]][pos[0]] = 0
    flashes += len(flashed)
    flashed = []

print(flashes)
