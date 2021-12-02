# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/02

def read_file() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [(s[0], int(s[1])) for s in (line.split() for line in f.read().strip().split("\n"))]

def part1(commands: list) -> int:
    position, depth = 0, 0
    for com in commands:
        if com[0] == "forward":
            position += com[1]
        elif com[0] == "down":
            depth += com[1]
        else: #com[1] == "up"
            depth -= com[1]
    return position * depth
            

def part2(commands: list) -> int:
    position, depth, aim = 0, 0, 0
    for com in commands:
        if com[0] == "forward":
            position += com[1]
            depth += aim * com[1]
        elif com[0] == "down":
            aim += com[1]
        else: #com[1] == "up"
            aim -= com[1]
    return position * depth

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")