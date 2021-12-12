# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import part1, part2, read_file, parse_paths

def test():
    vals_1 = read_file("test_input_1.txt")
    vals_2 = read_file("test_input_2.txt")
    vals_3 = read_file("test_input_3.txt")
    paths_1 = parse_paths(vals_1)
    paths_2 = parse_paths(vals_2)
    paths_3 = parse_paths(vals_3)
    assert part1(paths_1) == 10
    assert part1(paths_2) == 19
    assert part1(paths_3) == 226
    print("Passed Part 1")
    assert part2(paths_1) == 36
    assert part2(paths_2) == 103
    assert part2(paths_3) == 3509
    print("Passed Part 2")

if __name__ == "__main__":
    test()
