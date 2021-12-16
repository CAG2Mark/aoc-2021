data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

num = []
for ch in data[0]:
    num += ("{0:b}".format(int(ch, 16))).rjust(4, "0")
num = ''.join(num)
# start inclusive
def parsePacket(start, sub_length=0, sub_packets = 0):
    # print(f"-- BEGINNING OF SUB PACKET: {start}, sublen {sub_length}, subpackets {sub_packets} --")
    versionsum = 0
    length_done = 0

    subpacket_vals = []
    
    while sub_length > 7 or sub_packets > 0:
        # print(f"Startpos now {start}, sublen {sub_length}, subpackets {sub_packets}")
        packet_length = 0

        packet = num[start:]
        version = int(packet[0:3], 2)
        # print(version)
        versionsum += version
        typeid = int(packet[3:6], 2)

        is_operator = typeid != 4
        
        # print(packet)

        if is_operator:

            length_type = int(packet[6])
            parsed = (0,0)
            length_done += 7
            packet_length += 7


            if length_type == 1:
                subpackets = int(packet[7:7+11], 2)
                parsed = parsePacket(start+7+11, sub_packets = subpackets)
                length_done += 11
                packet_length += 11
            else:
                sublength = int(packet[7:7+15], 2)
                parsed = parsePacket(start+7+15, sub_length = sublength)
                length_done += 15
                packet_length += 15

            versionsum += parsed[0]
            length_done += parsed[1]
            packet_length += parsed[1]
            sp = parsed[2]

            packet_val = 0
            if typeid == 0:
                packet_val = sum(sp)
            elif typeid == 1:
                packet_val = 1
                for x in sp: packet_val *= x
            elif typeid == 2:
                packet_val = min(sp)
            elif typeid == 3:
                packet_val = max(sp)
            elif typeid == 5:
                packet_val = sp[0] > sp[1]
            elif typeid == 6:
                packet_val = sp[0] < sp[1]
            elif typeid == 7:
                packet_val = sp[0] == sp[1]

            subpacket_vals.append(packet_val)

        else:
            i = 0
            val = ""
            while True:
                will_end = packet[6+5*i] == "0"
                val += packet[6+5*i+1:6+5*i+5]
                i += 1
                if will_end: break
            length_done += 6 + 5*i
            packet_length += 6 + 5*i
            val = int(val, 2)
            
            subpacket_vals.append(val)

        sub_length -= packet_length
        sub_packets -= 1
        start += packet_length
    # print(f"-- END OF RECURSION --")
    return (versionsum, length_done, subpacket_vals)

v = parsePacket(0, sub_length = len(num))

print(v[2][0])
            


