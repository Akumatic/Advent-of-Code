# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/6

def read_file(filename: str = "input.txt") -> str:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return f.readline().strip()

def part1(datastream: str) -> int:
    i = 4
    while len(set(datastream[(i-4):i])) != 4:
        i += 1
    return i

def part2(datastream: str) -> int:
    i = 14
    while len(set(datastream[(i-14):i])) != 14:
        i += 1
    return i

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
