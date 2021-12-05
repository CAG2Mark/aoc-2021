data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

points = []
for ln in data:
    split = ln.split(" -> ")
    split1 = split[0].split(",")
    split2 = split[1].split(",")
    points.append(((int(split1[0]), int(split1[1])), (int(split2[0]), int(split2[1]))))
grid = {}

def cnt_point(point):
    if point in grid: grid[point] += 1
    else: grid[point] = 1

def o_range(x1, x2):
    if x2 > x1: return range(x1, x2+1)
    else: return range(x2, x1+1)
for p in points:
    if p[0][0] == p[1][0]:
        for y in o_range(p[0][1], p[1][1]):
            cnt_point((p[0][0], y))
    elif p[0][1] == p[1][1]:
        for x in o_range(p[0][0], p[1][0]):
            cnt_point((x, p[0][1]))
cnt = 0
for key in grid:
    if grid[key] > 1: cnt += 1
print(cnt)



    
