# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic
#
# https://adventofcode.com/2019/day/2

import sys, os
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import intcode, intcode_test

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(num) for num in f.readline().split(",")]

def part1(pc: intcode.Computer) -> int:
    pc.data[1], pc.data[2] = 12, 2
    pc.run()
    return pc.data[0]

def part2(pc: intcode.Computer) -> int:
    for noun in range(100):
        for verb in range(100):
            pc.reset()
            pc.data[1], pc.data[2] = noun, verb
            pc.run()
            if pc.data[0] == 19690720:
                return 100 * noun + verb

if __name__ == "__main__":
    intcode_test.test_02()
    pc = intcode.Computer(readFile())
    print(f"Part 1: {part1(pc)}")
    print(f"Part 2: {part2(pc)}")