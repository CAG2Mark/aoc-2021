data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]

expected = {
    "{": "}",
    "<": ">",
    "(": ")",
    "[": "]"
        }
points = {
    ")":1,
    "]":2,
    "}":3,
    ">":4
        }

def get_points(line):
    stack = []
    for c in line:
        if c in expected:
            stack.append(c)
        else:
            if not stack: 
                return points[c]
            last = stack.pop(len(stack)-1)
            if not c == expected[last]:
                return 0
    stack.reverse()
    total = 0
    for c in stack:
        total *= 5
        total += points[expected[c]]
    return total

points_ = []
for line in data:
    p = get_points(line)
    if p: points_.append(p)

points_.sort()
print(points_)
print(len(points_))
print( points_[(len(points_))//2])
