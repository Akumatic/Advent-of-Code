# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/06

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [int(x) for x in f.read().strip().split(",")]

def part1(vals: list, days: int = 80) -> int:
    fishes = vals[:]
    for _ in range(days):
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                fishes.append(8)
            else:
                fishes[i] -= 1
    return len(fishes)

def part2(vals: list, days: int = 256) -> int:
    fishes = [vals.count(x) for x in range(9)]
    for _ in range(days):
        tmp = fishes[0]
        fishes = fishes[1:] + [tmp]
        fishes[6] += tmp
    return sum(fishes)
                
if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")