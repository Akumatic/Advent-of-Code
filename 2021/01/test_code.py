# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import part1, part2

def test():
    vals = [199,200,208,210,200,207,240,269,260,263]
    assert part1(vals) == 7
    print("Passed Part 1")
    assert part2(vals) == 5
    print("Passed Part 2")

if __name__ == "__main__":
    test()
