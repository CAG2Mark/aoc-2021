data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]


# generate all distinct rotation for 90deg 
# generated using wolfram alpha lol
sin = {0:0, 1:1, 2:0, 3:-1}
cos = {0:1, 1:0, 2:-1, 3:0}
temp = {}
for x in range(4):
    for y in range(4):
        for z in range(4):
            r0c0 = cos[y]*cos[z]
            r0c1 = - cos[y] * sin[z]
            r0c2 = sin[y]
            r1c0 = sin[x] * sin[y] * cos[z] + cos[x] * sin[z]
            r1c1 = cos[x] * cos[z] - sin[x] * sin[y] * sin[z]
            r1c2 = -sin[x] * cos[y]
            r2c0 = sin[x] * sin[z] - cos[x] * sin[y] * cos[z]
            r2c1 = cos[x] * sin[y] * sin[z] + sin[x]* cos[z]
            r2c2 = cos[x] * cos[y]
            mat = (r0c0, r0c1, r0c2, r1c0, r1c1, r1c2, r2c0, r2c1, r2c2)
            temp[mat] = 0
matrices = [x for x in temp]
#print(matrices)
#print(len(matrices))
class Scanner:
    def __init__(self, scanner_id):
        self.scanner_id:int = scanner_id
        self.beacons:list = []

    def add_beacon(self, x,y,z):
        self.beacons.append((x,y,z))

    def gen_possibilities(self):
        possibilities = []
        for x in matrices:
            pos = []
            for b in self.beacons:
                p = b[0]
                q = b[1]
                r = b[2]
                poss = (\
                        p * x[0] + q * x[1] + r * x[2],\
                        p * x[3] + q * x[4] + r * x[5],\
                        p * x[6] + q * x[7] + r * x[8]
                        )
                pos.append(poss)
            possibilities.append(pos)

        return possibilities

scanners = {}
scanner:Scanner = Scanner(-1)
for ln in data:
    if "scanner" in ln:
        num = int(ln[12:-4])
        scanner = Scanner(num)
    elif ln.strip():
        ln = ln.split(",")
        scanner.add_beacon(int(ln[0]), int(ln[1]), int(ln[2]))
    else:
        scanners[scanner.scanner_id] = scanner
        scanner = Scanner(-1)

if scanner.scanner_id != -1: scanners[scanner.scanner_id] = scanner

# how much b1s has to move perfectly overlap with one point in b2s
def gen_deltas(b1s, b2s):
    d = {}
    deltas = []
    for b1 in b1s:
        for b2 in b2s:
            delta = tuple([b2[i] - b1[i] for i in range(3)])
            if not delta in d:
                d[delta] = 0
                deltas.append(delta)
    return deltas

todo = [0]
unknown = [k for k in scanners]
unknown.remove(0)
all_deltas = {0: (0,0,0)}
beacons = {}

while todo:
    s_id = todo.pop()
    cur = scanners[s_id]

    for b in cur.beacons:
        if not b in beacons: beacons[b] = 1
        else: beacons[b] += 1

    # compare against all unknown scanners
    for s__id in unknown.copy():

        print(s_id, s__id, unknown)
        cur2 = scanners[s__id]
        ps = cur2.gen_possibilities()
        flag = False
        for that in ps:
            this = cur.beacons
            deltas = gen_deltas(this, that)
            # check all possible offsets until found one where 12 or more overlap
            # deltas = [(68,-1246,-43)]
            # deltas = [(0,0,0)]
            for delta in deltas:
                that_offset = [(b[0] - delta[0], b[1] - delta[1], b[2] - delta[2]) for b in that]
                # print(delta)
                # print(that_offset)
                # print()
                d = {}
                conc = this + that_offset
                for b in conc:
                    if not b in d: d[b] = 1
                    else: d[b] += 1
                d = [d[b]-1 for b in d]
                if sum(d) >= 12:
                    print(f"match found: {cur.scanner_id}, {cur2.scanner_id}")
                    # overwrite all beacons in the second scanner with the correctly oriented ones
                    # and also transform them to the first beacon's position
                    
                    cur2.beacons = that_offset
                        
                    all_deltas[cur2.scanner_id] = delta
                    for b in that_offset:
                        if not b in beacons: beacons[b] = 1
                        else: beacons[b] += 1

                    todo.append(cur2.scanner_id)
                    unknown.remove(cur2.scanner_id)

                    flag = True
                    break
                if flag:
                    break
            if flag: break

beacons = [k for k in beacons]
print(len(beacons))

b_file = open("input2", "w")
b_file.write(str([all_deltas[k] for k in all_deltas]))
