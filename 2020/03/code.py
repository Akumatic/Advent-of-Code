# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
# https://adventofcode.com/2020/day/3

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line[:-1] for line in f.readlines()]

def count_trees(vals: list, dx: int, dy: int) -> int:
    x, y, cnt, length, mod = 0, 0, 0, len(vals) - dy, len(vals[0])
    while y < length:
        x = (x + dx) % mod
        y += dy
        if vals[y][x] == "#":
            cnt += 1
    return cnt

def part1(vals: list) -> int:
    return count_trees(vals, 3, 1)

def part2(vals: list, sol_part1: int) -> int:
    deltas = ((1, 1), (5, 1), (7, 1), (1, 2))
    prod = sol_part1
    for delta in deltas:
        prod *= count_trees(vals, delta[0], delta[1])
    return prod

def test():
    test_input = ["..##.......", "#...#...#..", ".#....#..#.",
    "..#.#...#.#", ".#...##..#.", "..#.##.....", ".#.#.#....#",
    ".#........#", "#.##...#...", "#...##....#", ".#..#...#.#"]
    assert part1(test_input) == 7
    assert part2(test_input, 7) == 336

if __name__ == "__main__":
    test()
    vals = readFile()
    sol_part1 = part1(vals)
    print(f"Part 1: {sol_part1}")
    print(f"Part 2: {part2(vals, sol_part1)}")