# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/9

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [(line.split()[0], int(line.split()[1])) for line in f.readlines()]

def simulate_moves(instructions: list, knots: int) -> int:
    pos = [[0, 0] for _ in range(knots)]
    tail_history = {(0, 0)}
    for dir, steps in instructions:
        for _ in range(steps):
            # head movement
            pos[0][0] += {"R": 1, "L": -1}.get(dir, 0)
            pos[0][1] += {"U": 1, "D": -1}.get(dir, 0)
            # following knots movement
            for i in range(1, knots):
                dx = pos[i-1][0] - pos[i][0]
                dy = pos[i-1][1] - pos[i][1]
                dist = (dx**2 + dy**2)**0.5
                if dist < 2.0:
                    continue
                if dist == 2.0:
                    pos[i][0] += (dx // 2)
                    pos[i][1] += (dy // 2)
                else: # dist > 2.0:
                    pos[i][0] += (dx // abs(dx))
                    pos[i][1] += (dy // abs(dy))
            tail_history.add((pos[-1][0], pos[-1][1]))
    return len(tail_history)

def part1(vals: list) -> int:
    return simulate_moves(vals, 2)

def part2(vals: list) -> int:
    return simulate_moves(vals, 10)

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
