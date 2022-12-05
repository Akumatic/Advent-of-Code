# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/4

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        pairs = [line.strip().split(",") for line in f.readlines()]
    return [(range(*[int(x) for x in pair[0].split("-")]), range(*[int(x) for x in pair[1].split("-")])) for pair in pairs]

def range_overlaps(r1: range, r2: range) -> bool:
    return r1.start <= r2.start and r1.stop >= r2.start or r2.start <= r1.start and r2.stop >= r1.start

def range_fully_contains(r1: range, r2: range) -> bool:
    return r1.start >= r2.start and r1.stop <= r2.stop or r2.start >= r1.start and r2.stop <= r1.stop

def part1(vals: list) -> int:
    return sum(1 for pairs in vals if range_fully_contains(*pairs))

def part2(vals: list) -> int:
    return sum([1 for pairs in vals if range_overlaps(*pairs)])

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
