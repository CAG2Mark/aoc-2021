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
    print(fold)
    for i in range(fold[1]+1, 2*fold[1]+1):
        mirror = (fold[1] - i + fold[1])
        if mirror < 0: continue
        for j in range(N):
            if fold[0]:
                if dots[j][i]: 
                    print((i,j), "to", (mirror,j))
                    dots[j][mirror] = dots[j][i]
                    dots[j][i] = 0
            else:
                if dots[i][j]: 
                    print((j,i), "to", (j,mirror))
                    dots[mirror][j] = dots[i][j]
                    dots[i][j] = 0
    break #part 1

sm = 0
for row in dots:
    sm += sum(row)

print(sm)
