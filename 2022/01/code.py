# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/1

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        groups = [group for group in f.read().strip().split("\n\n")]
    return [sum(int(i) for i in group.split("\n")) for group in groups]

def part1(vals: list) -> int:
        return sorted(vals)[-1]

def part2(vals: list) -> int:
        return sum(sorted(vals)[-3:])

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")