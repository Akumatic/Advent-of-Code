# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/03

def read_file() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [line for line in f.read().strip().split("\n")]

def get_mcb(vals: list) -> list:
    bit_count = [sum(int(num[i]) for num in vals) for i in range(len(vals[0]))]
    return [1 if cnt >= (len(vals) - cnt) else 0 for cnt in bit_count]

def reduce_reports(reports: list, invert: bool = False) -> int:
    for i in range(0, len(reports[0])):
        mcb = get_mcb(reports)[i]
        bit = str(mcb if not invert else 1 - mcb)
        reports = [rep for rep in reports if rep[i] == bit]
        if len(reports) == 1:
            break
    return int(reports[0], 2)

def part1(vals: list) -> int:
    mcb = get_mcb(vals)
    gamma = "".join(["1" if bit else "0" for bit in mcb])
    epsilon = "".join(["0" if bit else "1" for bit in mcb])
    return int(gamma, 2) * int(epsilon, 2)
            
def part2(vals: list) -> int:
    ogr = reduce_reports(vals[:]) # oxygen generator rating
    csr = reduce_reports(vals[:], invert=True) # CO2 scrubber rating
    return ogr * csr

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(vals)}")
    print(f"Part 2: {part2(vals)}")