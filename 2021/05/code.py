# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/05

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        lines = [line.split(" -> ") for line in f.read().strip().split("\n")]
    return [[(int(s[0]), int(s[1])) for s in (x.split(",") for x in line)] for line in lines]

def count_crossings(vals: list, allow_diagonal: bool = False) -> int:
    segments = dict()
    for val in vals:
        x1, x2, y1, y2 = val[0][0], val[1][0], val[0][1], val[1][1]
        x_dir = 1 if x1 < x2 else -1 if x1 > x2 else 0
        y_dir = 1 if y1 < y2 else -1 if y1 > y2 else 0
        dist = max(abs(x2 - x1), abs(y2 - y1))
        cond = True if allow_diagonal else (x_dir == 0 or y_dir == 0)
        tmp = [(x1 + n*x_dir, y1 + n*y_dir) for n in range(dist + 1) if cond]

        for segment in tmp:
            if segment not in segments:
                segments[segment] = 1
            else:
                segments[segment] += 1

    return sum(1 for x in segments if segments[x] > 1)

def part1(vals: list) -> int:
    return count_crossings(vals)
            
def part2(vals: list) -> int:
    return count_crossings(vals, allow_diagonal=True)
                
if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")