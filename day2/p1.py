data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

hpos = 0
depth = 0
for x in data:
    if not x.strip(): continue
    parsed = x.split(" ")
    if parsed[0] == "forward":
        hpos += int(parsed[1])
    elif parsed[0] == "down":
        depth += int(parsed[1])
    else:
        depth -= int(parsed[1])

print(hpos*depth)
