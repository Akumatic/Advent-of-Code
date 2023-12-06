# SPDX-License-Identifier: MIT
# Copyright (c) 2023 Akumatic
#
# https://adventofcode.com/2023/day/1

import re

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [line.strip() for line in f.readlines()]

def get_simple_calibration_value(line: str) -> int:
    nums = re.findall(r'\d', line)
    return 10 * int(nums[0]) + int(nums[-1])

def get_real_calibration_value(line: str) -> int:
    mapping = {"one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    nums = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    return 10 * (mapping.get(nums[0]) or int(nums[0])) + (mapping.get(nums[-1]) or int(nums[-1]))

def part1(vals: list) -> int:
    return sum(get_simple_calibration_value(val) for val in vals)

def part2(vals: list) -> int:
    return sum(get_real_calibration_value(val) for val in vals)


if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")