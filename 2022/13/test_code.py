# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic

from code import read_file, part1, part2

def test():
    vals = read_file("test_input.txt")
    assert part1(vals) == 13
    print("Passed Part 1")
    assert part2(vals) == 140
    print("Passed Part 2")

if __name__ == "__main__":
    test()
