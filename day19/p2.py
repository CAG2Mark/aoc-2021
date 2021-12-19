import ast

data = open("input2").read().split("\n")[0]
print(data)
data = ast.literal_eval(data)

max_ = 0
max_i = 0
max_j = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        a = data[i]
        b = data[j]
        dist = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
        if dist > max_: 
            max_i = i
            max_j = j
            max_ = dist

print(max_, max_i, max_j)
