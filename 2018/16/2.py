import sys
import re

all_oppcodes = [
    "addr", "addi", 
    "mulr", "muli", 
    "banr", "bani", 
    "borr", "bori", 
    "setr", "seti", 
    "gtir", "gtri", "gtrr",
    "eqir", "eqri", "eqrr"
]
def apply(instruction, registers):
    oppcode, a, b, c = instruction
    result = [v for v in registers]
    match oppcode:
        case "addr": result[c] = registers[a] + registers[b]
        case "addi": result[c] = registers[a] + b

        case "mulr": result[c] = registers[a] * registers[b]
        case "muli": result[c] = registers[a] * b

        case "banr": result[c] = registers[a] & registers[b]
        case "bani": result[c] = registers[a] & b

        case "borr": result[c] = registers[a] | registers[b]
        case "bori": result[c] = registers[a] | b

        case "setr": result[c] = registers[a]
        case "seti": result[c] = a

        case "gtir": result[c] = 1 if a > registers[b] else 0
        case "gtri": result[c] = 1 if registers[a] > b else 0
        case "gtrr": result[c] = 1 if registers[a] > registers[b] else 0

        case "eqir": result[c] = 1 if a == registers[b] else 0
        case "eqri": result[c] = 1 if registers[a] == b else 0
        case "eqrr": result[c] = 1 if registers[a] == registers[b] else 0
    return result

samples, program = list(sys.stdin.read().split("\n\n\n\n"))
sample_blocks = samples.split("\n\n")

possible_mappings = [ set(all_oppcodes) for _ in range(16)]
for b in sample_blocks:
    lines = b.splitlines()
    registers_before = list(map(int, re.findall(r"\d+", lines[0])))
    instruction = list(map(int, re.findall(r"\d+", lines[1])))
    registers_after = list(map(int, re.findall(r"\d+", lines[2])))
    
    compatible_oppcodes = set(oppcode for oppcode in all_oppcodes if apply((oppcode, *instruction[1:]), registers_before) == registers_after)
    possible_mappings[instruction[0]] &= compatible_oppcodes

import networkx as nx
G = nx.Graph([(n1, n2) for n1 in range(16) for n2 in possible_mappings[n1]])
mapping = nx.bipartite.maximum_matching(G, top_nodes=range(16))

registers = [0] * 4
for line in program.splitlines():
    instruction = list(map(int, re.findall(r"\d+", line)))
    registers = apply((mapping[instruction[0]], *instruction[1:]) , registers)
print(registers[0])
