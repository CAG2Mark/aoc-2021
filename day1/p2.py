data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
data = [int(x) for x in data]
cnt = 0
for i in range(2,len(data)-1):
    if data[i-2]+data[i-1]+data[i] < data[i-1]+data[i]+data[i+1]: cnt += 1

print(cnt)