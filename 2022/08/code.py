# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/8

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        lines = [[int(x) for x in line.strip()] for line in f.readlines()]
    return lines

def calculate_scenic_score(field: list, i: int, j: int) -> int:
    dirs = {"u": (0, -1), "d": (0, 1), "l": (1, 0), "r": (-1, 0)}
    count = {"u": 0, "d": 0, "l": 0, "r": 0}
    for dir, val in dirs.items():
        x, y = i, j
        while x + val[0] >= 0 and x + val[0] < len(field[0]) and \
                y + val[1] >= 0 and y + val[1] < len(field):
            x += val[0]
            y += val[1]
            count[dir] += 1
            if field[y][x] >= field[j][i]: 
                break
    return count["u"] * count["d"] * count["l"] * count["r"]

def part1(vals: list) -> int:
    return sum([any((
        not any(vals[j][x] >= vals[j][i] for x in range(0, i)), # left
        not any(vals[j][x] >= vals[j][i] for x in range(i+1, len(vals[0]))), # right
        not any(vals[y][i] >= vals[j][i] for y in range(0, j)), # down
        not any(vals[y][i] >= vals[j][i] for y in range(j+1, len(vals))) # up
    )) for j in range(len(vals)) for i in range(len(vals[0]))])

def part2(vals: list) -> int:    
    scenic_scores = [calculate_scenic_score(vals, i, j) for 
        j in range(len(vals)) for i in range(len(vals[0]))]
    return max(scenic_scores)

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
