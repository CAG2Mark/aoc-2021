data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

steps = []
for ln in data:
    ln = ln.split(" ")
    on = ln[0] == "on"
    ln = ln[1]
    ln = ln.split(",")
    a = []
    a.append(on)
    for l in ln:
        l = l.split("=")[1]
        l = l.split("..")
        p = int(l[0])
        q = int(l[1])
        a.append((min(p,q), max(p,q)))
    a = tuple(a)
    steps.append(a)

done = []

cnt = 0

class Cuboid:
    def __init__(self, x1, x2, y1, y2, z1, z2, is_on=False):
        if x2 < x1 or y2 < y1 or z2 < z1:
            self.x1 = -1
            return
        self.x1:int = x1
        self.x2:int = x2
        self.y1:int = y1
        self.y2:int = y2
        self.z1:int = z1
        self.z2:int = z2
        self.is_on:bool = is_on

    def __bool__(self):
        return self.x1 != -1

    def get_volume(self):
        return (self.x2-self.x1+1)*(self.y2-self.y1+1)*(self.z2-self.z1+1)

    def __str__(self):
        return f"(x:({self.x1}, {self.x2}), y:({self.y1}, {self.y2}), z:({self.z1}, {self.z2}), vol: {self.get_volume()})"

null_cuboid = Cuboid(-1,-1,-1,-1,-1,-1)

def find_overlap(c1:Cuboid, c2:Cuboid) -> Cuboid:
    if not c1 or not c2: return null_cuboid
    return Cuboid(max(c1.x1, c2.x1), min(c1.x2, c2.x2), \
            max(c1.y1, c2.y1), min(c1.y2, c2.y2),
            max(c1.z1, c2.z1), min(c1.z2, c2.z2), True)

## -- I DO NOT TAKE CREDIT FOR THIS SOLUTION -- ##
# I got general idea for this elegant solution from Lekro https://github.com/lekro.
# However, before implementing, I made sure to fully understand the idea behind it.
cuboids = []
vol = 0
for step in steps:
    c = Cuboid(step[1][0], step[1][1], step[2][0], step[2][1], step[3][0], step[3][1], step[0])
    if step[0]: vol += c.get_volume()
    # remove intersections, regardless of whether it is on or off we remove intersections
    # with other cuboids
    for i in range(len(cuboids)):
        prev = cuboids[i]
        overlap = find_overlap(c, prev)
        if not overlap: continue
        # these 4 lines make use of the inclusion exclusion principle.
        # the intersections are stored and then cumulatively intersected
        # again with the newly added cuboids, alternating the on state
        # for each newly added cuboid as per the inclusion exclusion
        # principle
        if prev.is_on: vol -= overlap.get_volume()
        else: vol += overlap.get_volume()
        overlap.is_on = not prev.is_on
        cuboids.append(overlap)
   
    if step[0]:
        cuboids.append(c)

print(vol)

