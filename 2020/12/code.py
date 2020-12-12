# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
#https://adventofcode.com/2020/day/12

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def part1(input: list) -> int:
    x, y = 0, 0
    dirs = ((1,0), (0, 1), (-1, 0), (0, -1))
    idx = 0
    for instruction in input:
        action = instruction[0]
        value = int(instruction[1:])
        if action == "N":
            y += value
        elif action == "S":
            y -= value
        elif action == "E":
            x += value
        elif action == "W":
            x -= value
        elif action == "F":
            x += dirs[idx][0] * value
            y += dirs[idx][1] * value
        else: # action in ("R", "L")
            sig = 1 if action == "L" else -1
            idx = (idx + sig * value // 90) % 4
    return abs(x) + abs(y)

def part2(input: list) -> int:
    x, y, wx, wy = 0, 0, 10, 1
    dirs = ((1,1), (-1, 1), (-1, -1), (1, -1))
    idx = 0
    for instruction in input:
        action = instruction[0]
        value = int(instruction[1:])
        if action == "N":
            wy += value
        elif action == "S":
            wy -= value
        elif action == "E":
            wx += value
        elif action == "W":
            wx -= value
        elif action == "F":
            x += wx * value
            y += wy * value
        else: # action in ("R", "L")
            sig = 1 if action == "L" else -1
            for _ in range(value // 90):
                idx_prev, idx = idx, (idx + sig) % 4
                tmp_wx = wx
                wx = wy * dirs[idx_prev][1] * dirs[idx][0]
                wy = tmp_wx * dirs[idx_prev][0] * dirs[idx][1]
    return abs(x) + abs(y)

if __name__ == "__main__":
    input = readFile()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")