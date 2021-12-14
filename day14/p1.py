data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]

template = list(data[0])
pairs = {}
for i in range(2,len(data)):
    ln = data[i].split(" -> ")
    pairs[ln[0]] = ln[1]

template = list(template)

N = 10
for _ in range(N):
    i = 0
    L = len(template)
    diff = 0
    while i < L + diff - 1:
        cur = template[i] + template[i+1]
        if cur in pairs:
            template.insert(i+1, pairs[cur])
            i += 1
            diff += 1
        i += 1

cnt = {}
for ch in template:
    if ch in cnt: cnt[ch] += 1
    else: cnt[ch] = 1
cnt = [cnt[ch] for ch in cnt]
cnt.sort()
print(cnt[-1] - cnt[0])
