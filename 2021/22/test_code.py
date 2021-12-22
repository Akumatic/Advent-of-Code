# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import *

def test():
    instructions = [read_file(f"test_input_{i}.txt") for i in range(1, 4)]
    assert part1(instructions[0]) == 39
    print("Passed short Part 1")
    assert part1(instructions[1]) == 590784
    print("Passed long Part 1")
    assert part2(instructions[0]) == 39
    assert part1(instructions[2]) == 474140
    assert part2(instructions[2]) == 2758514936282235
    print("Passed Part 2")

if __name__ == "__main__":
    test()
