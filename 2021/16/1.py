import sys

hexstring = input()
bits = bin(int(hexstring, 16))[2:].zfill(len(hexstring) * 4)
index = 0

def read_int(size):
    global index
    res = int(bits[index:index+size], 2)
    index += size
    return res

def read_literal():
    global index
    res = ""
    while True:
        res += bits[index+1:index+5]
        index += 5
        if bits[index-5] == '0':
            break;
    return int(res, 2)

def read_packet():
    version = read_int(3)
    id = read_int(3)
    if id == 4:
        literal = read_literal()
        return (version, id, literal, [])
    else:
        sub_packets = []
        mode = read_int(1)
        if mode == 0:
            total_length = read_int(15)
            end_index = index + total_length
            while index < end_index:
                sub_packets.append(read_packet())
        else:
            nb_packets = read_int(11)
            for _ in range(nb_packets):
                sub_packets.append(read_packet())

        version += sum(p[0] for p in sub_packets)                
        return (version, id, None, sub_packets)

print(read_packet()[0])
