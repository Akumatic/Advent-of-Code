# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
#https://adventofcode.com/2020/day/14

def readFile() -> tuple:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line.strip().split(" = ") for line in f.readlines()]

def recursive_floating_bits(value: int, idx: list) -> list:
    if len(idx) == 1:
        return [value | (1 << idx[0]), value & ~(1 << idx[0])]
    return recursive_floating_bits(value | (1 << idx[0]), idx[1:]) + \
        recursive_floating_bits(value & ~(1 << idx[0]), idx[1:])

def mask_index(value: int, mask: str) -> list:
    # if bitmask bit is 1, memory address bit is overwritten with 1
    value |= int(mask.replace("X", "0"), 2)
    # take care of all floating bits
    positions = [35 - i for i, char in enumerate(mask) if char == "X"]
    return recursive_floating_bits(value, positions)

def run_v2(input: list) -> dict: 
    memory = dict()
    mask = None
    for instruction in input:
        if instruction[0] == "mask":
            mask = instruction[1]
        else: # instruction[0][:3] == "mem"
            value = int(instruction[1])
            indices = mask_index(int(instruction[0][4:-1]), mask)
            for idx in indices:
                memory[idx] = value
    return memory

def run_v1(input: list) -> dict:
    mask_and, mask_or = None, None
    memory = dict()
    for instruction in input:
        if instruction[0] == "mask":
            mask_and = int(instruction[1].replace("X", "1"), 2)
            mask_or = int(instruction[1].replace("X", "0"), 2)
        else: # instruction[0][:3] == "mem"
            idx = int(instruction[0][4:-1])
            value = (int(instruction[1]) & mask_and) | mask_or
            memory[idx] = value
    return memory

def part1(input: list) -> int:
    return sum(run_v1(input).values())

def part2(input: list) -> int:
    return sum(run_v2(input).values())

if __name__ == "__main__":
    input = readFile()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")