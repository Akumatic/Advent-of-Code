# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import part1, part2

def test():
    vals = [("forward", 5), ("down", 5), ("forward", 8), ("up", 3), ("down", 8), ("forward", 2)]
    assert part1(vals) == 150
    print("Passed Part 1")
    assert part2(vals) == 900
    print("Passed Part 2")

if __name__ == "__main__":
    test()
