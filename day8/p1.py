data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]
cnt = 0
for ln in data:
    ln = ln.split(" | ")[1].split(" ")
    for d in ln:
        cnt += len(d) == 2 or len(d) == 3 or len(d) == 4 or len(d) == 7
print(cnt)
