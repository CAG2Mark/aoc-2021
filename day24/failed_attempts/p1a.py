data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

# hidden constraint with input: for some reason they always multiply x and y
# by 0 after each input before doing anything to them

# solve manually later (or maybe not?)
mem = {}
prevop = {}
mem["x"] = "0"
mem["y"] = "0"
mem["z"] = "0"
mem["w"] = "0"
prevop["x"] = "none"
prevop["y"] = "none"
prevop["z"] = "none"
prevop["w"] = "none"

ops = {"add": "+", "mul":"*", "mod":"%", "mult":"*", "div":"//", "eql":"=="}
input_cnt = 0
for ln in data:
    spl = ln.split(" ")
    if spl[0] == "inp":
        input_cnt += 1
        mem["w"] = "i" + str(input_cnt)
    else:
        val1 = mem[spl[1]]
        val2 = spl[2]
        val2 = val2 if val2.strip("-").isnumeric() else mem[val2]
        flag = False
        if spl[0] == "mul":
            if val1 == "0" or val2 == "0":
                mem[spl[1]] = "0"
                flag = True
            #elif val2 == "1":
            #    mem[spl[1]] = val2
            #    flag = True
            #elif val1 == "1":
            #    mem[spl[1]] = val2
            #    flag = True
        #if spl[0] == "div" and val2 == "1": flag = True
        #if spl[0] == "add": 
        #    if val2 == "0": 
        #        flag = True
        #    if val1 == "0":
        #        mem[spl[1]] = val2
        #        flag = True
        #if val1.strip("-").isnumeric() and spl[0] == "mod" and \
        #        val2.strip("-").isnumeric() and int(val2) > int(val1): flag = True
        #if spl[0] == "eql" and val1.strip("-").isnumeric() and not (0 < int(val1) < 10) \
        #        and val2[0] == "i" and val2[1:].isnumeric(): 
        #            mem[spl[1]] = "0"
        #            flag = True
        if spl[0] == "mod" and prevop[spl[1]] == "eql": flag = True

        if not flag:
            mem[spl[1]] = f"({val1}){ops[spl[0]]}({val2})"
            if not "i" in mem[spl[1]]:
                mem[spl[1]] = str(int(eval(mem[spl[1]])))
    prevop[spl[1]] = spl[0]
    print(ln)
    print(f"{spl[1]} = {mem[spl[1]]}")

# print(mem)
