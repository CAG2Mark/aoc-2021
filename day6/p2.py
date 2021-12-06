data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]
data = [int(x) for x in data[0].split(",")]

tickDic = []
for i in range(7):
    tickDic.append([0,0])

for d in data:
    tickDic[d][0] += 1

for i in range(256):
    curTick = i%7
    tickDic[(curTick+2)%7][1] += tickDic[curTick][0]
    tickDic[curTick][0] += tickDic[curTick][1]
    tickDic[curTick][1] = 0

sm = 0
for t in tickDic:
    sm += t[0]
    sm += t[1]

print(sm)
