# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
""" https://adventofcode.com/2020/day/2 """

def readFile() -> list:
    input = list()
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        for line in f.readlines():
            txt = line.split()
            nums = txt[0].split("-")
            input.append((int(nums[0]), int(nums[1]), txt[1][:1], txt[2]))
    return input

def part1(vals: list) -> int:
    cnt = 0
    for val in vals:
        min, max, char, text = val # for better readability
        char_cnt = text.count(char)
        if char_cnt >= min and char_cnt <= max:
            cnt += 1
    return cnt

def part2(vals: list) -> int:
    cnt = 0
    for val in vals:
        pos_a, pos_b, char, text = val # for better readability
        if (char == text[pos_a - 1]) ^ (char == text[pos_b - 1]):
            cnt += 1
    return cnt

def test():
    test_input = [(1, 3, "a", "abcde"), 
        (1, 3, "b", "cdefg"), (2, 9, "c", "ccccccccc")]
    assert part1(test_input) == 2
    assert part2(test_input) == 1

if __name__ == "__main__":
    test()
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")