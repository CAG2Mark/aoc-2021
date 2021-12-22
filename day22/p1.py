data = open("input.test").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

steps = []
for ln in data:
    ln = ln.split(" ")
    on = ln[0] == "on"
    ln = ln[1]
    ln = ln.split(",")
    a = []
    a.append(on)
    for l in ln:
        l = l.split("=")[1]
        l = l.split("..")
        p = int(l[0])
        q = int(l[1])
        a.append((min(p,q), max(p,q)))
    a = tuple(a)
    steps.append(a)

grid = {}

def valid(pos):
    return -50 <= pos[0] <= 50 and \
            -50 <= pos[1] <= 50 and \
            -50 <= pos[2] <= 50

for step in steps:
    for z in range(max(-50, step[3][0]), min(51, step[3][1] + 1)):
        for y in range(max(-50, step[2][0]), min(51, step[2][1] + 1)):
            for x in range(max(-50, step[1][0]), min(51, step[1][1] + 1)):
                pos = (x,y,z)
                if valid(pos):
                    grid[pos] = step[0]

grid = [grid[k] for k in grid]
print(sum(grid))

