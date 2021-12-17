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

time_map = {}

# try all from 0 to 1000

for i in range(-1000,1000):
    time = 0
    y_vel = i
    y_pos = 0
    max_temp = 0
    while y_pos > y_high:
        y_pos += y_vel
        y_vel -= 1
        time += 1
    
    if not (y_low <= y_pos <= y_high): continue # this is not a valid y
    
    time_high = time - 1

    while y_pos >= y_low:
        y_pos += y_vel
        y_vel -= 1
        time_high += 1

    time_map[i] = (time, time_high)

validcnt = 0
# possible x
for y_vel in time_map:
    for i in range(0,1000):
        t = time_map[y_vel][0]
        t_high = time_map[y_vel][1]
        x_travel = 0
        x_vel = i
        x_pos = 0

        flag = False
        for time in range(1,t_high+1):
            x_pos += x_vel
            
            sgn = 0 if x_vel == 0 else (1 if x_vel > 0 else -1)
            x_vel = x_vel - sgn

            if (x_vel == 0 or t <= time <= t_high) and (x_low <= x_pos <= x_high):
                flag = True
                break

            if x_pos > x_high:
                flag = False
                break


        if not flag: continue
        validcnt += 1



print(validcnt)
