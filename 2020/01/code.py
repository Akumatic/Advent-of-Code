# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
#https://adventofcode.com/2020/day/1

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(line[:-1]) for line in f.readlines()]

def part1(vals: list) -> int:
    for val in vals:
        if (2020 - val) in vals:
            return (2020 - val) * val

def part2(vals: list) -> int:
    for i in range(len(vals)):
        for j in range(i, len(vals)):
            if (2020 - vals[i] - vals[j]) in vals:
                return vals[i] * vals[j] *  (2020 - vals[i] - vals[j])


def test():
    test_input = [1721, 979, 366, 299, 675, 1456]
    assert part1(test_input) == 514579
    assert part2(test_input) == 241861950

if __name__ == "__main__":
    test()
    vals = readFile()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")