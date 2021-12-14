data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]

template = list(data[0])
pairs = {}
paircnt = {}
elemcnt = {}
for i in range(2,len(data)):
    ln = data[i].split(" -> ")
    pairs[ln[0]] = (ln[0][0] + ln[1], ln[1] + ln[0][1])
    paircnt[ln[0]] = 0
    elemcnt[ln[0][0]] = 0
    elemcnt[ln[0][1]] = 0 

for ch in template:
    elemcnt[ch] += 1

for i in range(len(template) - 1):
    cur = template[i] + template[i+1]
    if cur in paircnt: paircnt[cur] += 1

N = 40
for _ in range(N):
    temp = paircnt.copy()
    for k in pairs:
        cnt = paircnt[k]
        if cnt == 0: continue
        temp[k] -= cnt
        elemcnt[pairs[k][0][1]] += cnt
        for p in pairs[k]:
            temp[p] += cnt
    paircnt = temp

elemcnt = [elemcnt[k] for k in elemcnt]
elemcnt.sort()
print(elemcnt[-1] - elemcnt[0])

