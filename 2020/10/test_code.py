# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic

from code import part1, part2

def test():
    input = [16,10,15,5,1,11,7,19,6,12,4]
    tmp = input[:]
    tmp.sort()
    assert part1(tmp) == 35
    assert part2(tmp) == 8
    print("Passed tests for", input)

    input = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
    tmp = input[:]
    tmp.sort()
    assert part1(tmp) == 220
    assert part2(tmp) == 19208
    print("Passed tests for", input)

if __name__ == "__main__":
    test()