data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

class Execution:
    def __init__(self, k1, k2, k3):
        self.k1:int = k1
        self.k2:int = k2
        self.k3:int = k3

    def get_possible_inputs(self, target):
        target_og = target
        possible = []
        for I in range(1, 10):
            part2 = I + self.k2
            target_ = target - part2
            
            # generate possible ranges of zn for this input
            range1 = range((target-2)*self.k3, (target+2)*self.k3+1)
            range2 = range((target_-2)*self.k3, (target_+2)*self.k3+1)
            range3 = range(((target-1)*self.k3-2)//26 - 26, ((target+1)*self.k3+2)//26+27)
            range4 = range(((target_-1)*self.k3-2)//26 - 26, ((target_+1)*self.k3+2)//26+27)

            merged = list(range1) + list(range2) + list(range3) + list(range4)
            merged = list(dict.fromkeys(merged)) # remove duplicates
            for zn in merged:
                xn = zn % 26 + self.k1
                zn_ = zn // self.k3

                c1 = 1 if xn == I else 26
                c2 = 0 if xn == I else 1

                zn_1 = c1 * zn_ + c2 * part2
                if zn_1 == target_og:
                    possible.append((zn, I))
        return possible

executions = []

k1 = 0
k2 = 0
k3 = 0
for i in range(1,len(data)):
    ln = data[i]
    if i % 18 == 0: executions.append(Execution(k1, k2, k3))
    else:
        val = ln.split(" ")[2]
        if i % 18 == 4: k3 = int(val)
        elif i % 18 == 5: k1 = int(val)
        elif i % 18 == 15: k2 = int(val)

executions.append(Execution(k1, k2, k3))
executions.reverse()
memo = {}
def solve(position, cur_input, target):
    if position == 14:
        # print(target)
        if target != 0: return []
        return [""]
    e = executions[position]
    x = e.get_possible_inputs(target)
    solves = []
    # print(position, x, target, e.k1, e.k2, e.k3)
    for p in x:
        reqd_z = p[0]
        cur_in = p[1]
        next_pos = (position+1, cur_in, reqd_z)
        this_solves = []
        if not next_pos in memo:
            memo[next_pos] = solve(position+1, str(cur_in), reqd_z)
            
        this_solves = memo[next_pos]

        for s in this_solves:
            solves.append(s + str(cur_in))
    return solves

x = solve(0, "", 0)
x.sort()
print("max: ", x[0], " min: ", x[-1])
# solve(5, "", 108505)
