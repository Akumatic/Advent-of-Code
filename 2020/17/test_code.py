# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic

from code import part1, part2, parse_input

def test():
    input = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]
    data = parse_input(input)
    assert part1(data) == 112
    print(f"Passed part 1")
    assert part2(data) == 848
    print(f"Passed part 2")

if __name__ == "__main__":
    test()