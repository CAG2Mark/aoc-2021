data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

def normalise(x):
    x = list(x)
    x.sort()
    return ''.join(x)

def findMissing(x):
    all_ = list("abcdefg")
    for a in x: all_.remove(a)
    return all_

segments={
        "abcefg":0,
        "cf":1,
        "acdeg":2,
        "acdfg":3,
        "bcdf":4,
        "abdfg":5,
        "abdefg":6,
        "acf":7,
        "abcdefg":8,
        "abcdfg":9
        }

sm = 0

for ln in data:

    de = {
        "a":"",
        "b":"",
        "c":"",
        "d":"",
        "e":"",
        "f":"",
        "g":"",

        }
    ln = ln.split(" | ")
    datain = ln[0].split(" ")
    dataout = ln[1].split(" ")
    
    datain = [normalise(x) for x in datain]
    
    # find 1,4,7,8
    one = ""
    four = ""
    seven = ""
    eight = ""
    for x in datain:
        if len(x) == 2: one = x
        elif len(x) == 4: four = x
        elif len(x) == 3: seven = x
        elif len(x) == 7: eight = x

    # compare 1 and 7 to find "a"
    seven_ = list(seven)
    for c in one: seven_.remove(c)

    de["a"] = seven_[0]

    six = ""
    # compare 1 to find a 6 to find c and f
    for x in datain:
        if len(x) == 6 and ((one[0] in x) ^ (one[1] in x)):
            six = x
            if one[0] in x:
                de["c"] = one[1]
                de["f"] = one[0]
            else:
                de["c"] = one[0]
                de["f"] = one[1]

    zero = ""
    # find a 0 using 4 and 9
    for x in datain:
        if x == six: continue #0,6,9 are the only ones missing one
        if len(x) != 6: continue

        # 0 does not have the middle segment but 6 does,
        # and 6's missing segment is not one of the
        # unknown segments in 4
        
        # find missing segment
        missing = findMissing(x)[0]

        if missing == de["c"]: continue
        if not missing in four: continue
        zero = x
        de["d"] = missing

    three = ""
    five = ""
    two = ""
    # find a 3 and 5 and 2
    for x in datain:
        if len(x) != 5: continue

        if de["c"] in x and de["f"] in x:
            three = x
            three_ = list(three)
            three_.remove(de["a"])
            three_.remove(de["c"])
            three_.remove(de["f"])
            three_.remove(de["d"])
            de["g"] = three_[0]
        elif de["c"] in x and not de["f"] in x:
            two = x
        else:
            five = x

    # find "e" using 2
    two_ = list(two)
    two_.remove(de["a"])
    two_.remove(de["c"])
    two_.remove(de["d"])
    two_.remove(de["g"])
    de["e"] = two_[0]

    # find "b" using 5
    five_ = list(five)
    five_.remove(de["a"])
    five_.remove(de["f"])
    five_.remove(de["d"])
    five_.remove(de["g"])
    de["b"] = five_[0]

    digit = ""
    de_ = {}
    for k in de:
        de_[de[k]] = k

    for x in dataout:
        x = list(x)
        for i, c in enumerate(x):
            x[i] = de_[c]
        num = segments[normalise(''.join(x))]
        digit += str(num)
    sm += int(digit)

print(sm)

    
    
