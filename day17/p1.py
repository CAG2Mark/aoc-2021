data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

ln = data[0]
ln = ln.split(" ")
xpart = ln[2].split("..")
ypart = ln[3].split("..")

x_low = int(xpart[0][2:])
x_high = int(xpart[1][:-1])
y_low = int(ypart[0][2:])
y_high = int(ypart[1])

max_y_vel = y_high - y_low + 1

# try all from 0 to 1000

max_height = 0
max_vel = 0
for i in range(0,1000):
    y_vel = i
    y_pos = 0
    max_temp = 0
    while y_pos > y_high:
        y_pos += y_vel
        if y_pos > max_temp:
            max_temp = y_pos
        y_vel -= 1

    if y_low <= y_pos <= y_high: max_height = max_temp

print(max_height)
print(max_vel) 
