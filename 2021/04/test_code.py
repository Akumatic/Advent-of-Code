# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import part1, part2, read_file

def test():
    draws, fields = read_file("test_input.txt")
    assert part1(draws, fields) == 4512
    print("Passed Part 1")
    assert part2(draws, fields) == 1924
    print("Passed Part 2")

if __name__ == "__main__":
    test()
