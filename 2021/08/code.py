# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/08

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [(s[0].split(), s[1].split()) for s in (line.split(" | ") for line in f.read().strip().split("\n"))]

def remove_from_pattern(pattern: str, mask: str) -> str:
    return "".join(s for s in pattern if s not in mask)

def find_correct_mapping(patterns: list, mask: str) -> str:
    for pattern in patterns:
        tmp = "".join(s for s in pattern if s not in mask)
        if len(tmp) == 1:
            return tmp

def determine_mapping(patterns: list) -> dict:
    mapping = dict()
    p = [[x for x in patterns if len(x) == l] for l in range(2, 8)]
    # directly determinable
    mapping["a"] = remove_from_pattern(p[1][0], p[0][0])
    # determine g by excluding a & 4 from 9
    mapping["g"] = find_correct_mapping(p[4], p[2][0] + mapping["a"])
    # determine e by excluding a, g & 4 from 8
    mapping["e"] = remove_from_pattern(p[5][0], p[2][0] + mapping["a"] + mapping["g"])
    # determine b by excluding a, e, g & 1 from 8
    mapping["b"] = find_correct_mapping(p[4], p[0][0] + mapping["a"] + mapping["e"] + mapping["g"])
    # determine d by excluding b & 1 from 4
    mapping["d"] = remove_from_pattern(p[2][0], mapping["b"] + p[0][0])
    #determine f by excluding a, b, d & g from 5
    mapping["f"] = find_correct_mapping(p[3], mapping["a"] + mapping["b"] + mapping["d"] + mapping["g"])
    # determine c by excluding f from 1
    mapping["c"] = remove_from_pattern(p[0][0], mapping["f"])
    return mapping
    
def determine_output(output: str, mapping: dict) -> int:
    digits = {"abcefg" : 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5,
        "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}
    tmp = [mapping[x] for x in output]
    tmp.sort()
    return digits["".join(tmp)]

def part1(vals: list) -> int:
    count = 0
    for val in vals:
        count += sum(1 for x in val[1] if len(x) in [2, 3, 4, 7])
    return count

def part2(vals: list) -> int:
    result = 0
    for val in vals:
        mapping = determine_mapping(val[0])
        decode_mapping = {mapping[key]: key for key in mapping}
        tmp = [determine_output(x, decode_mapping) for x in val[1]]
        result += 1000 * tmp[0] + 100 * tmp[1] + 10 * tmp[2] + tmp[3]
    return result
    
if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")