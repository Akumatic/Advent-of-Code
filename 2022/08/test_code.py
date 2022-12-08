# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic

from code import read_file, part1, part2, calculate_scenic_score

def test():
    vals = read_file("test_input.txt")
    assert part1(vals) == 21
    print("Passed Part 1")
    assert calculate_scenic_score(vals, 2, 1) == 4
    assert calculate_scenic_score(vals, 2, 3) == 8
    assert part2(vals) == 8
    print("Passed Part 2")

if __name__ == "__main__":
    test()
