import sys

def compute_segment_signature(digits):
    sig = { s : [0] * 8 for s in "abcdefg" }
    for d in digits:
        for segment in d:
            sig[segment][len(d)] += 1
    return sig

digits = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
segment_signatures = compute_segment_signature(digits)

res = 0
for line in sys.stdin.read().splitlines():
    pattern_list, output_list = line.split("|")

    pattern_signatures = compute_segment_signature(pattern_list.strip().split(" "))
    mapping = {}
    for unkown_segment, unknown_sig in pattern_signatures.items():
        for segment, segment_sig in segment_signatures.items():
            if unknown_sig == segment_sig:
                mapping.update({unkown_segment : segment})

    displayed = 0
    for digit in output_list.strip().split(" "):
        displayed = 10 * displayed + digits.index("".join(sorted([mapping[s] for s in digit])))
    res += displayed

print(res)
