data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

gamma = 0
epsilon = 0
N = len(data[0])
for i in range(N):
    zeroCnt = 0
    oneCnt = 0
    weight = 1<<i
    for ln in data:
        if ln[-i-1] == "0": zeroCnt += 1
        else: oneCnt += 1
    if oneCnt > zeroCnt: gamma += weight
    else: epsilon += weight

print(gamma*epsilon)
