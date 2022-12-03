# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/3

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [line.strip() for line in f.readlines()]

def split_items(items: str) -> tuple:
    half_size = len(items) // 2
    return (items[:half_size], items[half_size:])

def get_dupes(comp_a: list, comp_b: list, comp_c: list = None) -> list:
    return set([item for item in comp_a if (item in comp_b) and (item in comp_c if comp_c else True)])

def get_priority(item: str) -> int:
    return ord(item) - 38 if ord(item) < 96 else ord(item) - 96

def part1(vals: list) -> int:
    return sum([sum([get_priority(item) for item in get_dupes(*split_items(items))]) for items in(vals)])

def part2(vals: list) -> int:
    groups = [(vals[i], vals[i+1], vals[i+2]) for i in range(0, len(vals), 3)]
    return sum([sum([get_priority(item) for item in get_dupes(*group)]) for group in groups])

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
