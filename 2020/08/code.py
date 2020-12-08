# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
#https://adventofcode.com/2020/day/8

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line.split() for line in f.read().strip().split("\n")]

def run(instructions: list) -> tuple:
    accumulator = 0
    pointer = 0
    visited = []
    size = len(instructions)
    while pointer not in visited and pointer != size:
        visited.append(pointer)
        if instructions[pointer][0] == "acc":
            accumulator += int(instructions[pointer][1])
            pointer += 1
        elif instructions[pointer][0] == "jmp":
            pointer += int(instructions[pointer][1])
        else: # instructions[pointer][0] == "nop":
            pointer += 1
    return pointer, accumulator

def part1(instructions: list) -> int:
    return run(instructions)[1]

def part2(instructions: list) -> int:
    size = len(instructions)
    for i in range(size):
        if instructions[i][0] == "jmp":
            instructions[i][0] = "nop"
            pointer, accumulator = run(instructions)
            instructions[i][0] = "jmp"

        elif instructions[i][0] == "nop":
            instructions[i][0] = "jmp"
            pointer, accumulator = run(instructions)
            instructions[i][0] = "nop"

        else: # instructions[i][0] == "acc"
            continue 

        if pointer == size:
            return accumulator


if __name__ == "__main__":
    instructions = readFile()
    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")