# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import part1, part2, read_file, expand

def test():
    vals = read_file("test_input_1.txt")
    assert part1(vals) == 40
    print("Passed Part 1")
    assert expand(vals) == read_file("test_input_2.txt")
    print("Passed expansion")
    assert part2(vals) == 315
    print("Passed Part 2")

if __name__ == "__main__":
    test()
