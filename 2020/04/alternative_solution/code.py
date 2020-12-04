# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
# https://adventofcode.com/2020/day/4

import passport

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line[:-1] for line in f.readlines()]

def parse_data(vals: list) -> list:
    result = list()
    cur = list()
    for line in vals:
        if line:
            cur += line.split(" ")
        else:
            result.append(passport.Pass(cur))
            cur.clear()
            
    # since last line is not "", add data from cur once more
    result.append(passport.Pass(cur))
    return result

def part1(passports: list) -> int:
    return sum(p.valid_fields() for p in passports)

def part2(passports: list) -> int:
    return sum(p.valid_data() for p in passports)

if __name__ == "__main__":
    from test_code import test
    test()
    passports = parse_data(readFile())
    print(f"Part 1: {part1(passports)}")
    print(f"Part 2: {part2(passports)}")