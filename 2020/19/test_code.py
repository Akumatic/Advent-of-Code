# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic

from code import part1, part2, parse_rules
import re

def test():
    input = ['0: 1 2','1: "a"','2: 1 3 | 3 1','3: "b"']
    assert part1(parse_rules(input), ["aab", "aba"]) == 2
    input = ['0: 4 1 5','1: 2 3 | 3 2','2: 4 4 | 5 5',
        '3: 4 5 | 5 4','4: "a"','5: "b"']
    words = ["ababbb","bababa","abbbab","aaabbb","aaaabbb"]
    assert part1(parse_rules(input), words) == 2
    print(f"Passed Part 1")

if __name__ == "__main__":
    test()