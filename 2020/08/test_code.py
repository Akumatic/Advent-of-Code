# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic

from code import part1, part2

def test():
    instructions = [["nop", "+0"], ["acc", "+1"], ["jmp", "+4"], 
    ["acc", "+3"], ["jmp", "-3"], ["acc", "-99"], ["acc", "+1"], ["jmp", "-4"], ["acc", "+6"]]
    assert(part1(instructions) == 5)
    assert part2(instructions) == 8

if __name__ == "__main__":
    test()