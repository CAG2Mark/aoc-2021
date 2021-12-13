data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]

dots = []
folds = []

N = 1500
for i in range(N):
    dots.append([0]*N)
foldmode = False
for ln in data:
    if not ln:
        foldmode = True
        continue
    if foldmode:
        ln = ln.split(" ")[2].split("=")
        folds.append((ln[0] == "x", int(ln[1])))
    else:
        ln = ln.split(",")
        dots[int(ln[1])][int(ln[0])] = 1

for fold in folds:
    for i in range(fold[1]+1, 2*fold[1]+1):
        mirror = (fold[1] - i + fold[1])
        if mirror < 0: continue
        for j in range(N):
            if fold[0]:
                if dots[j][i]: 
                    dots[j][mirror] = dots[j][i]
                    dots[j][i] = 0
            else:
                if dots[i][j]: 
                    dots[mirror][j] = dots[i][j]
                    dots[i][j] = 0
max_x = 0
max_y = 0
for y in range(N):
    for x in range(N):
        if dots[y][x]:
            if max_x < x: max_x = x
            if max_y < y: max_y = y

for y in range(max_y+1):
    for x in range(max_x+1):
        print("#" if dots[y][x] else ".", end="")
    print()
