data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]
data = [int(x) for x in data[0].split(",")]

for _ in range(80):
    for i in range(len(data)):
        data[i] -= 1
        if data[i] == -1:
            data[i] = 6
            data.append(8)

print(len(data))
