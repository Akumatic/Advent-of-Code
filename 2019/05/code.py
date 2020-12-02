# SPDX-License-Identifier: MIT
# Copyright (c) 2019 Akumatic
# 
# https://adventofcode.com/2019/day/5

import sys, os
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import intcode

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(num) for num in f.readline().split(",")]

def part1(vals: list) -> int:
    return intcode.getOutput(vals.copy(), input=1)

def part2(vals: list) -> int:
    return intcode.getOutput(vals.copy(), input=5)

def test():
    assert intcode.parseCode(1001) == (1, 0, 1, 0)
    assert intcode.getOutput([1,0,0,0,99]) == 2
    assert intcode.getOutput([1,1,1,4,99,5,6,0,99]) == 30
    assert intcode.getOutput([3,0,4,0,99], input=42) == 42
    assert intcode.getOutput([1101,100,-1,4,0], getVals=True) == [1101,100,-1,4,99]
    assert intcode.getOutput([3,9,8,9,10,9,4,9,99,-1,8], input=0) == 0
    assert intcode.getOutput([3,9,8,9,10,9,4,9,99,-1,8], input=8) == 1
    assert intcode.getOutput([3,9,7,9,10,9,4,9,99,-1,8], input=0) == 1
    assert intcode.getOutput([3,9,7,9,10,9,4,9,99,-1,8], input=8) == 0
    assert intcode.getOutput([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], input=0) == 0
    assert intcode.getOutput([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], input=1) == 1
    assert intcode.getOutput([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], input=0) == 0 
    assert intcode.getOutput([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], input=1) == 1
    assert intcode.getOutput([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,
        1101,1000,1,20,4,20,1105,1,46,98,99], input=0) == 999
    assert intcode.getOutput([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,
        1101,1000,1,20,4,20,1105,1,46,98,99], input=8) == 1000
    assert intcode.getOutput([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,
        1101,1000,1,20,4,20,1105,1,46,98,99], input=9) == 1001

if __name__ == "__main__":
    test()
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")