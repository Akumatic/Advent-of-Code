# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic

from code import part1, part2, run_v1, run_v2

def test():
    input = [["mask", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"],
        ["mem[8]", "11"],["mem[7]", "101"],["mem[8]", "0"]]
    assert run_v1(input) == {7:101, 8:64}
    assert part1(input) == 165
    print(f"Passed part 1 for {input}")
    input = [["mask","000000000000000000000000000000X1001X"], ["mem[42]","100"],
        ["mask","00000000000000000000000000000000X0XX"], ["mem[26]","1"]]
    assert run_v2(input) == {26:1, 27:1, 58:100,
        59:100, 16:1,17:1, 18:1, 19:1, 24:1, 25:1}
    assert part2(input) == 208
    print(f"Passed part 2 for {input}")

if __name__ == "__main__":
    test()