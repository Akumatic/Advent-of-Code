# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic

from code import read_file, run_instructions, part1, part2

def test():
    vals = read_file("test_input.txt")
    assert run_instructions([["noop"], ["addx", "3"], ["addx", "-5"]]) == [1, 1, 1, 4, 4]
    assert part1(vals) == 13140
    print("Passed Part 1")
    assert part2(vals) == "\n".join(
        ["","##..##..##..##..##..##..##..##..##..##..","###...###...###...###...###...###...###.",
        "####....####....####....####....####....","#####.....#####.....#####.....#####.....",
        "######......######......######......####","#######.......#######.......#######.....", ""])
    print("Passed Part 2")

if __name__ == "__main__":
    test()
