# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic
# 
# https://adventofcode.com/2019/day/9

import sys, os
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import intcode

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(num) for num in f.readline().split(",")]

def part1(vals: list) -> int:
    return intcode.getOutput(vals.copy(), input=1)

def part2(vals: list) -> int:
    return intcode.getOutput(vals.copy(), input=2)

def test():
    assert intcode.getOutput([104,1125899906842624,99]) == 1125899906842624
    assert len(str(intcode.getOutput([1102,34915192,34915192,7,4,7,99,0]))) == 16

if __name__ == "__main__":
    test()
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")