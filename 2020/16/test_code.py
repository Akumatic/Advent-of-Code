# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic

from code import part1, part2, parseInput, get_valid_tickets, get_possible_positions, determine_positions

def test():
    input = [
        ["class: 1-3 or 5-7", "row: 6-11 or 33-44", "seat: 13-40 or 45-50"],
        ["your ticket:", "7,1,14"],
        ["nearby tickets:", "7,3,47", "40,4,50", "55,2,20", "38,6,12"]
    ]
    data = parseInput(input)
    assert part1(data) == 71
    print(f"Passed part 1")

    input = [
        ["class: 0-1 or 4-19", "row: 0-5 or 8-19", "seat: 0-13 or 16-19"],
        ["your ticket:", "11,12,13"],
        ["nearby tickets:", "3,9,18", "15,1,5", "5,14,9"]
    ]
    data = parseInput(input)
    valid_tickets = get_valid_tickets(data)
    possible_positions = get_possible_positions(data["rules"], valid_tickets)
    positions = determine_positions(possible_positions)
    assert positions == {"row": 0, "class": 1, "seat": 2}
    assert data["you"][positions["class"]] == 12
    assert data["you"][positions["row"]]== 11
    assert data["you"][positions["seat"]] == 13
    print(f"Passed part 2")

if __name__ == "__main__":
    test()