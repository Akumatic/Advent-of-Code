# SPDX-License-Identifier: MIT
# Copyright (c) 2023 Akumatic
#
# https://adventofcode.com/2023/day/3

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        return f.read().strip().split("\n")

def check_surrounding_fields(vals: list, x: int, y: int) -> bool:
    return any(
        vals[y + j][x + i] != "." and not vals[y + j][x + i].isdigit()
        for i in range(-1, 2) for j in range(-1, 2)
        if 0 <= x + i < len(vals[0]) and 0 <= y + j < len(vals)
    )

def sum_part_numbers(vals: list) -> int:
    num_sum = 0
    for y in range(len(vals)):
        valid = False
        num = 0
        for x in range(len(vals[0])):
            if not vals[y][x].isdigit():
                if valid:
                    num_sum += num
                    valid = False
                num = 0
                continue
            num = num * 10 + int(vals[y][x])
            if not valid:
                valid = check_surrounding_fields(vals, x, y)
        if valid:
            num_sum += num
    return num_sum

def find_possible_gears(vals: list) -> list:
    positions = list()
    for y in range(len(vals)):
        positions.extend([(x, y) for x, char in enumerate(vals[y]) if vals[y][x] == "*"])
    return positions

def check_left_of_symbol(vals: list, x, y) -> int:
    if not 0 <= y < len(vals):
        return -1
    i, num = 1, 0
    check = False
    while (x - i) >= 0 and vals[y][x - i].isdigit():
        check = True
        num += int(vals[y][x - i]) * 10**(i - 1)
        i += 1
    return num if check else -1

def check_right_of_symbol(vals:list, x, y) -> int:
    if not 0 <= y < len(vals):
        return -1
    i, num = 1, 0
    check = False
    while (x + i) < len(vals[y]) and vals[y][x + i].isdigit():
        check = True
        num = num * 10 + int(vals[y][x + i])
        i += 1
    return num if check else -1

def determine_gear_ratios(vals: list, possible_gears: list) -> list:
    result = list()
    for x, y in possible_gears:
        part_numbers = list()
        for j in (-1, 0, 1):
            tmp_l = check_left_of_symbol(vals, x, y + j)
            tmp_r = check_right_of_symbol(vals, x, y + j)
            tmp_m = vals[y + j][x] if 0 <= y + j < len(vals) and vals[y + j][x].isdigit() else None
            if tmp_m is not None:
                nums = [int("".join([str(x) for x in (tmp_l, tmp_m, tmp_r) if x != -1]))]
            else:
                nums = [x for x in (tmp_l, tmp_r) if x != -1]
            part_numbers.extend(nums)
        if len(part_numbers) == 2:
            result.append(part_numbers[0] * part_numbers[1])
    return result

def part1(vals: list) -> int:
    return sum_part_numbers(vals)

def part2(vals: list) -> int:
    possible_gears = find_possible_gears(vals)
    return sum(determine_gear_ratios(vals, possible_gears))

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")