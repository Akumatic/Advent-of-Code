# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import part1, part2, read_file, brute_force

def test():
    vals = read_file("test_input.txt")  
    vals = brute_force(vals)
    assert part1(vals) == 45
    print("Passed Part 1")
    assert part2(vals) == 112
    print("Passed Part 2")

if __name__ == "__main__":
    test()
