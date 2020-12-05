# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
# https://adventofcode.com/2020/day/5

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line[:-1] for line in f.readlines()]

def parse(seat) -> tuple:
    return sum([2**(6-i) for i in range(7) if seat[i] in ("B")]), \
        sum([2**(9-i) for i in range(7, 10) if seat[i] in ("R")])

def part1(seat_ids: list) -> int:
    return max(seat_ids)

def part2(seat_ids: list) -> int:
    for i in range(8, 1015): # front and back row skipped
        if i not in seat_ids and (i - 1) in seat_ids and (i + 1) in seat_ids:
            return i

def test():
    assert parse("FBFBBFFRLR") == (44,5)
    assert parse("BFFFBBFRRR") == (70,7)
    assert parse("FFFBBBFRRR") == (14,7)
    assert parse("BBFFBBFRLL") == (102,4)

if __name__ == "__main__":
    test()
    seats = [parse(val) for val in readFile()]
    seat_ids = [seat[0]*8 + seat[1] for seat in seats]
    print(f"Part 1: {part1(seat_ids)}")
    print(f"Part 2: {part2(seat_ids)}")