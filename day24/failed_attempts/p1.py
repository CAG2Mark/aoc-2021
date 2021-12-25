data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

def run_data(input_data):
    mem = {"x": 0, "y": 0, "z": 0, "w": 0}
    
    pos = 0
    for ln in data:
        if ln[0] == "i": 
            print()
            print(f"pos {13 - pos}:")
        print("x:{} y:{} z:{} w:{} \t{}".format(mem["x"], mem["y"], mem["z"], mem["w"], ln))
        split = ln.split()
        instruc = split[0]
        first = split[1]
        if instruc == "inp":
            mem[first] = int(input_data[pos])
            pos += 1
            continue
        second = split[2]

        first_val:int = mem[first]
        second_val:int = mem[second] if second in mem else int(second)

        if instruc == "add":
            mem[first] = first_val + second_val
        elif instruc == "mul":
            mem[first] = first_val * second_val
        elif instruc == "div":
            if second_val == 0:
                print("Error: div by 0")
                return
            mem[first] = first_val // second_val
        elif instruc == "mod":
            if second_val == 0:
                print("Error: mod by zero")
                return
            mem[first] = first_val % second_val
        elif instruc == "eql":
            mem[first] = int(first_val == second_val)

    print(mem["z"])

input_cnt = sum([1 if "inp" in ln else 0 for ln in data])

val_str = input()

run_data(val_str)

