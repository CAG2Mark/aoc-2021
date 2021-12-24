data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

ops = {"add": "+", "mul":"*", "mod":"%", "mult":"*", "div":"/", "eql":"=="}

cnt = 0
cnta = 0
for ln in data:
    cnt += 1
    if not cnt % 10: print()
    line = ""
    spl = ln.split(" ")
    if spl[0] == "inp":
        cnta += 1
        print(f"cout << \"{cnta}:\" << z << endl; {spl[1]} = i{cnta};", end = "")
    else:
        print(f"{spl[1]} = {spl[1]} {ops[spl[0]]} {spl[2]};", end = "")
