# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
#https://adventofcode.com/2020/day/16

def parseInput(blocks: list) -> dict:
    data = {"rules": dict(), "you": list(), "tickets": list()}
    # 1st block, rules
    for rule in blocks[0]:
        rule = rule.split(": ")
        data["rules"][rule[0]] = []
        vals = [int(n) for r in rule[1].split(" or ") for n in r.split("-")]
        for i in range(0, len(vals), 2):
            data["rules"][rule[0]].append(range(vals[i], vals[i+1] + 1))
    # 2nd block, your ticket
    data["you"] += [int(num) for num in blocks[1][1].split(",")]
    # 3rd block, nearby tickets
    for ticket in blocks[2][1:]:
        data["tickets"].append([int(num) for num in ticket.split(",")])
    return data

def readFile() -> dict:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        blocks = [block.split("\n") for block in f.read().strip().split("\n\n")]
    return parseInput(blocks)

def check_rule(rule: list, number: int) -> bool:
    return any([number in r for r in rule])

def check_rules(rules: dict, number: int) -> bool:
    for rule in rules:
        if check_rule(rules[rule], number):
            return True
    return False

def validate_ticket(rules: dict, ticket: list) -> bool:
    for number in ticket:
        if not check_rules(rules, number):
            return False
    return True

def get_valid_tickets(data: dict) -> list:
    valid_tickets = [data["you"]]
    for ticket in data["tickets"]:
        if validate_ticket(data["rules"], ticket):
            valid_tickets.append(ticket)
    return valid_tickets

def get_possible_positions(rules: dict, valid_tickets: list) -> dict:
    possible_positions = dict()
    size = len(rules)
    for rule in rules:
        pos = []
        for i in range(size):
            if all([check_rule(rules[rule], t[i]) for t in valid_tickets]):
                pos.append(i)
        possible_positions[rule] = pos
    return possible_positions

def determine_positions(possible_positions: dict) -> dict:
    positions = dict()
    keys = list(possible_positions.keys())
    while keys:
        for key in keys:
            if len(possible_positions[key]) == 1:
                positions[key] = possible_positions[key][0]
                keys.remove(key)
                for pos in keys:
                    if positions[key] in possible_positions[pos]:
                        possible_positions[pos].remove(positions[key])
                continue
    return positions

def part1(data: dict) -> int:
    error_rate = 0
    for ticket in data["tickets"]:
        for number in ticket:
            if not check_rules(data["rules"], number):
                error_rate += number
    return error_rate

def part2(data: dict) -> int:
    valid_tickets = get_valid_tickets(data)
    possible_positions = get_possible_positions(data["rules"], valid_tickets)
    positions = determine_positions(possible_positions)

    result = 1
    for rule in positions:
        if rule.startswith("departure"):
            result *= data["you"][positions[rule]]
    return result

if __name__ == "__main__":
    input = readFile()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")