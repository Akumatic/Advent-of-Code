# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/01

def read_file() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(line) for line in f.read().strip().split("\n")]

def part1(vals: list) -> int:
    return sum(vals[i+1] > vals[i] for i in range(len(vals) - 1))

def part2(vals: list) -> int:
    return sum(vals[i+3] + vals[i+2] + vals[i+1] > vals[i+2] + vals[i+1] + vals[i] 
                for i in range(len(vals) - 3))

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")