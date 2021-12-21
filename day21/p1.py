data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]
ln1 = data[0].split(" ")
p1pos = int(ln1[-1]) - 1
p1score = 0

ln2 = data[1].split(" ")
p2pos = int(ln2[-1]) - 1
p2score = 0

die = 0
diecnt = 0

tick = True
while p1score < 1000 and p2score < 1000:
    
    d1 = (die)%100 + 1
    d2 = (die+1)%100 + 1
    d3 = (die+2)%100 + 1

    if tick:
        p1pos += d1 + d2 + d3
        p1pos %= 10
        p1score += p1pos + 1
    else:
        p2pos += d1 + d2 + d3
        p2pos %= 10
        p2score += p2pos + 1
    tick = not tick
    die += 3
    diecnt += 3
    die %= 100

if p1score >= 1000:
    print(p2score * diecnt)
else:
    print(p1score * diecnt)
