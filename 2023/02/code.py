# SPDX-License-Identifier: MIT
# Copyright (c) 2023 Akumatic
#
# https://adventofcode.com/2023/day/2

import re

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return [parse_game(line.strip()) for line in f.readlines()]

def parse_game(game: str) -> list:
    result = list()
    sets = game.split(": ")[1].split("; ")
    for cubes in sets:
        numbers = [int(num) for num in re.findall(r'\d+', cubes)]
        colors = re.findall(r'(red|blue|green)', cubes)
        result.append(list(zip(numbers, colors)))
    return result

def game_is_possible(sets: list) -> bool:
    limits = {"red": 12, "green": 13, "blue": 14}
    return all(not any(cubes[0] > limits[cubes[1]] for cubes in _set) for _set in sets)

def calculate_power(sets: list) -> int:
    dice = {"red": 0, "green": 0, "blue": 0}
    for _set in sets:
        for cubes in _set:
            dice[cubes[1]] = max(cubes[0], dice[cubes[1]])
    return dice["red"] * dice["green"] * dice["blue"]

def part1(games: list) -> int:
    return sum(id + 1 for id, game in enumerate(games) if game_is_possible(game))

def part2(games: list) -> int:
    return sum(calculate_power(game) for game in games)

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")