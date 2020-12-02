# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic
#
# https://adventofcode.com/2019/day/2

import sys, os
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import intcode

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(num) for num in f.readline().split(",")]

def part1(vals: list) -> int:
    memory = vals.copy()
    memory[1], memory[2] = 12, 2
    return intcode.getOutput(memory)

def part2(vals: list) -> int:
    for noun in range(100):
        for verb in range(100):
            memory = vals.copy()
            memory[1], memory[2] = noun, verb
            if intcode.getOutput(memory) == 19690720:
                return 100 * noun + verb

if __name__ == "__main__":
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")