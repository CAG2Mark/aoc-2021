data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

oxygenList = data.copy()
co2List = data.copy()

oxygenRating = ""
co2Rating = ""

N = len(data[0])
for i in range(N):
    zeroCntOxygen = 0
    oneCntOxygen = 0

    zeroCntCo2 = 0
    oneCntCo2 = 0
    for ln in oxygenList:
        if ln[i] == "0": zeroCntOxygen += 1
        else: oneCntOxygen += 1
    
    for ln in co2List:
        if ln[i] == "0": zeroCntCo2 += 1
        else: oneCntCo2 += 1

    oxCommon = "0" if zeroCntOxygen > oneCntOxygen else "1"
    co2Common = "1" if zeroCntCo2 > oneCntCo2 else "0"
    
    oxygenList = list(filter(lambda ln: ln[i] != oxCommon, oxygenList))
    co2List = list(filter(lambda ln: ln[i] != co2Common, co2List))

    if len(oxygenList) == 1 and not oxygenRating:
        oxygenRating = oxygenList[0]
    
    if len(co2List) == 1 and not co2Rating:
        co2Rating = co2List[0]

oxygenRating = int(oxygenRating, 2)
co2Rating = int(co2Rating, 2)


print(oxygenRating)
print(co2Rating)

print(oxygenRating * co2Rating)

