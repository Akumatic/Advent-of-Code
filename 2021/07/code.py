# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/06

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [int(x) for x in f.read().strip().split(",")]

def calculate_distances(positions):
    return [[abs(p-r) for p in positions] for r in range(min(positions), max(positions)+1)]

def part1(vals: list) -> int:
    return min(sum(dists) for dists in calculate_distances(vals))

def part2(vals: list) -> int:
    return min(sum((d*d+d)//2 for d in dists) for dists in calculate_distances(vals))
                
if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")