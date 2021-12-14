# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/14

def read_file(filename: str = "input.txt") -> tuple:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        lines = [line for line in f.read().strip().split("\n")]
    template = lines[0]
    rules = {x[0]: x[1] for x in (line.split(" -> ") for line in lines[2:])}
    return template, rules

def add_to_dict(d: dict, key: str, val: int = 1):
    if key not in d:
        d[key] = val
    else:
        d[key] += val

def count(polymer: str, rules: dict, iterations: int) -> dict:
    pairs = dict()
    for i in range(len(polymer) - 1):
        add_to_dict(pairs, polymer[i] + polymer[i+1])

    for _ in range(iterations):
        tmp = dict()
        for pair in pairs:
            add_to_dict(tmp, pair[0] + rules[pair], pairs[pair])
            add_to_dict(tmp, rules[pair] + pair[1], pairs[pair])
        pairs = tmp

    elements = dict()
    for pair in pairs:
        add_to_dict(elements, pair[0], pairs[pair])
    add_to_dict(elements, polymer[-1])
    return elements

def part1(template: str, insertion_rules: dict) -> int:
    letters = count(template, insertion_rules, 10)
    return max(letters.values()) - min(letters.values())

def part2(template: str, insertion_rules: dict) -> int:
    letters = count(template, insertion_rules, 40)
    return max(letters.values()) - min(letters.values())
    
if __name__ == "__main__":
    vals = read_file() # vals[0] is the template, vals[1] the insertion rules
    print(f"Part 1: {part1(*vals)}")
    print(f"Part 2: {part2(*vals)}")
