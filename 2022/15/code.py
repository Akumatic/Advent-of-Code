# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/15

from re import findall

def read_file(filename: str = "input.txt") -> list:
    pattern = "Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.*)"
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [[int(x) for x in findall(pattern, line)[0]] for line in f.readlines()]

def combine_ranges(ranges: list) -> list:
    new_ranges = list()
    start, stop = ranges[0]
    for i in range(1, len(ranges)):
        if ranges[i][0] > stop:
            new_ranges.append(range(start, stop))
            start, stop = ranges[i]
            continue
        if ranges[i][1] > stop:
            stop = ranges[i][1]
    new_ranges.append(range(start, stop))
    return new_ranges

def get_blocked_ranges(coords: list, line: int, _min = float('-inf'), _max = float('inf')) -> list:
    ranges = list()
    for sx, sy, bx, by in coords:
        sb_dist = abs(bx - sx) + abs(by - sy)
        height_dist = abs(sy - line)
        if height_dist > sb_dist:
            continue
        x_min = max(sx - (sb_dist - height_dist), _min)
        x_max = min(sx + (sb_dist - height_dist), _max)
        ranges.append((x_min, x_max))
    return combine_ranges(sorted(ranges))

def part1(vals: list, test: bool = False) -> int:
    return sum(len(r) for r in get_blocked_ranges(vals, 10 if test else 2000000))

def part2(vals: list, test: bool = False) -> int:
    max_val = 20 if test else 4000000
    for i in range(max_val + 1):
        ranges = get_blocked_ranges(vals, i, 0, max_val)
        if len(ranges) > 1:
            return (ranges[0].stop + 1) * 4000000 + i

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
