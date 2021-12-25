# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/25

def parse_lines(lines: list) -> dict:
    x, y = len(lines[0]), len(lines)
    return {"x": x, "y": y, "grid": {(i, j): lines[j][i] for j in range(y) for i in range(x)}}

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return parse_lines([line for line in f.read().strip().split("\n")])

def move_herd(data: dict, herd: str) -> dict:
    new = {"x": data["x"], "y": data["y"], "grid": dict()}
    # take care of all moving cucumbers
    moving_positions = [pos for pos in data["grid"] if data["grid"][pos] == herd]
    for position in moving_positions:
        if can_move(data, position):
            new["grid"][get_next_position(data, position)] = data["grid"][position]
            new["grid"][position] = "."
        else: # position not in new["grid"]:
            new["grid"][position] = data["grid"][position]
    # take care of every other location
    for position in data["grid"]:
        if position not in new["grid"]:
            new["grid"][position] = data["grid"][position]
    return new

def move_all(data: dict) -> dict:
    return move_herd(move_herd(data, ">"), "v")

def get_next_position(data: dict, position: tuple) -> tuple:
    if data["grid"][position] == "v":
        return (position[0], (position[1] + 1) % data["y"])
    else: #data["grid"][position] == ">":
        return ((position[0] + 1) % data["x"], position[1])

def can_move(data: dict, position: tuple) -> bool:
    if data["grid"][position] == ".":
        return False
    return data["grid"][get_next_position(data, position)] == "."

def count_possible_steps(data: dict) -> int:
    return sum(int(can_move(data, pos)) for pos in data["grid"])

def part1(data: dict) -> int:
    count = 1
    while count_possible_steps(data) > 0:
        data = move_all(data)
        count += 1
    return count

def part2(data: dict) -> int:
    return 0 # not doable until all other 49 stars are done

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")
