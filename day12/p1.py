data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]

paths = {}

def addPath(p1,p2):
    if not p1 in paths: paths[p1] = []
    if not p2 in paths: paths[p2] = []
    paths[p1].append(p2)
    paths[p2].append(p1)

for ln in data:
    ln = ln.strip()
    ln = ln.split("-")
    addPath(ln[0], ln[1])

total = 0
def search(node="start", smallVisited = []):
    global total
    if node=="end":
        total += 1
        return
    isSmall = node != "start" and node.islower()
    if node in smallVisited: return
    smallVisited = smallVisited.copy()
    if isSmall: smallVisited.append(node)
    for path in paths[node]:
        if path != "start":
            search(path,smallVisited)
search()
print(total)



