# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic

from code import part1, part2

def test():
    test_input = (
        [('R', 4), ('U', 4), ('L', 3), ('D', 1), 
         ('R', 4), ('D', 1), ('L', 5), ('R', 2)],
        [('R', 5), ('U', 8), ('L', 8), ('D', 3), 
         ('R', 17), ('D', 10), ('L', 25), ('U', 20)]
    )
    assert part1(test_input[0]) == 13
    print("Passed Part 1")
    assert part2(test_input[1]) == 36
    print("Passed Part 2")

if __name__ == "__main__":
    test()
