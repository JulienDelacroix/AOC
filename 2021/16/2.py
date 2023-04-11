import sys
import functools

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

def compute_value(id, sub_values):
    if id == 0: return sum(sub_values)
    if id == 1: return functools.reduce(lambda r, v: r*v, sub_values)
    if id == 2: return min(sub_values)
    if id == 3: return max(sub_values)
    if id == 5: return 1 if sub_values[0] > sub_values[1] else 0
    if id == 6: return 1 if sub_values[0] < sub_values[1] else 0
    if id == 7: return 1 if sub_values[0] == sub_values[1] else 0
    return 0

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
        value = compute_value(id, [p[2] for p in sub_packets])
        return (version, id, value, sub_packets)

print(read_packet()[2])
