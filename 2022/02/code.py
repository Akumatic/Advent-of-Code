# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/2

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [map_moves(line.strip().split(" ")) for line in f.readlines()]

def map_moves(moves: tuple) -> tuple:
    return [ord(moves[0]) - 64, ord(moves[1]) - 87]

def calculate_points(player: int, opponent: int) -> int:
    diff = (opponent - player) % 3
    return player + (3 if diff == 0 else (6 if diff == 2 else 0))

def calculate_move(opponent: int, state: int) -> int:
    match state:
        case 2: # tie
            return 3 + opponent
        case 3: # win
            return 7 + opponent % 3
        case 1: # lose
            return 1 + (opponent + 1) % 3

def part1(vals: list) -> int:
    return sum(calculate_points(player, opponent) for opponent, player in vals)

def part2(vals: list) -> int:
    return sum(calculate_move(opponent, state) for opponent, state in vals)

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")