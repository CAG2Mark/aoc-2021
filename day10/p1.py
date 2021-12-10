data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]

expected = {
    "{": "}",
    "<": ">",
    "(": ")",
    "[": "]"
        }
points = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
        }
total = 0

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
                return points[c]
    return 0
                                
for line in data:
    total += get_points(line)
print(total)
