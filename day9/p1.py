data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
hmap = []
for x in data:
    hmap.append([int(c) for c in x])

risks = 0
for y, row in enumerate(hmap):
    for x, col in enumerate(row):
        if y != 0 and hmap[y-1][x] <= col: continue
        if y != len(hmap)-1 and hmap[y+1][x] <= col: continue
        if x != 0 and hmap[y][x-1] <= col: continue
        if x != len(row)-1 and hmap[y][x+1] <= col: continue
        risks += col + 1
print(risks)
