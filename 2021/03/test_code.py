# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import part1, part2

def test():
    vals = ["00100", "11110", "10110", "10111", "10101", "01111",
        "00111", "11100", "10000", "11001", "00010", "01010"]
    assert part1(vals) == 198
    print("Passed Part 1")
    assert part2(vals) == 230
    print("Passed Part 2")

if __name__ == "__main__":
    test()
