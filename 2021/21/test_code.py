# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import *

def test():
    vals = read_file("test_input.txt")
    assert part1(vals) == 739785    
    print("Passed Part 1")
    assert part2(vals) == 444356092776315
    print("Passed Part 2")

if __name__ == "__main__":
    test()
