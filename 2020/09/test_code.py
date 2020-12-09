# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic

from code import part1, part2

def test():
    input = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 
        117, 150, 182, 127, 219, 299, 277, 309, 579]
    assert part1(input, 5) == 127
    assert part2(input, 127) == 62

if __name__ == "__main__":
    test()