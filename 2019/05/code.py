# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic
# 
# https://adventofcode.com/2019/day/5

import sys, os
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import intcode, intcode_test

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(num) for num in f.readline().split(",")]

def part1(pc: intcode.Computer) -> int:
    pc.reset(input=1)
    pc.run()
    return pc.data[0]

def part2(pc: intcode.Computer) -> int:
    pc.reset(input=5)
    pc.run()
    return pc.data[0]

if __name__ == "__main__":
    intcode_test.test_05()
    pc = intcode.Computer(readFile())
    print(f"Part 1: {part1(pc)}")
    print(f"Part 2: {part2(pc)}")