# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic

from code import part1, part2

def test():
    input = ["F10","N3","F7","R90","F11"]
    assert part1(input) == 25
    assert part2(input) == 286
    print("Passed tests for", input)

if __name__ == "__main__":
    test()