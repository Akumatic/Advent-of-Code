# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
#https://adventofcode.com/2020/day/9

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [int(line) for line in f.read().strip().split("\n")]

def getSums(input, position, size):
    return [input[i] + input[j] 
        for i in range(position, position + size)
        for j in range(i + 1, position + size)
        if input[i] != input[j]
    ]

def part1(input: list, len_preamble: int = 25) -> int:
    size = len(input)
    cur_pos = 0
    sums = getSums(input, cur_pos, len_preamble)
    loop_size = size - len_preamble - 1
    while cur_pos < loop_size:
        if input[cur_pos + len_preamble] not in sums:
            return input[cur_pos + len_preamble]
        cur_pos += 1
        sums = getSums(input, cur_pos, len_preamble)

def part2(input: list, num: int) -> int:
    size = len(input)
    for i in range(size):
        sum = input[i]
        next = i+1
        while sum < num and next < size:
            sum += input[next]
            next += 1
        if sum == num:
            tmp = input[i:next-1]
            return min(tmp) + max(tmp)

if __name__ == "__main__":
    input = readFile()
    number = part1(input)
    print(f"Part 1: {number}")
    print(f"Part 2: {part2(input, number)}")