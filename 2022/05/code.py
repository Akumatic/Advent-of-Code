# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic
#
# https://adventofcode.com/2022/day/5

def read_file(filename: str = "input.txt") -> tuple:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        lines = f.read().split("\n\n")
    crates_input = lines[0].split("\n")
    amount = int(crates_input.pop()[-2])
    stacks = []
    for i in range(amount):
        stack = [stack[(i*4)+1] for stack in crates_input if stack[(i*4)+1] != " "]
        stack.reverse()
        stacks.append(stack)
    move_input = [line.replace("move ", "").replace(" from ", " ").replace(" to ", " ") 
        for line in lines[1].strip().split("\n")]
    moves = [[int(i) for i in move.split(" ")] for move in move_input]
    return stacks, moves

def part1(stacks: list, moves: list) -> str:
    stacks_cp = [stack[:] for stack in stacks]
    for move in moves:
        for _ in range(move[0]):
            stacks_cp[move[2] - 1].append(stacks_cp[move[1] - 1].pop())
    return "".join(stack[-1] for stack in stacks_cp)

def part2(stacks: list, moves: list) -> str:
    stacks_cp = [stack[:] for stack in stacks]
    for move in moves:
        stacks_cp[move[2] - 1].extend(stacks_cp[move[1] - 1][-move[0]:])
        stacks_cp[move[1] - 1] = stacks_cp[move[1] - 1][:-move[0]]
    return "".join(stack[-1] for stack in stacks_cp)

if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(*vals)}")
    print(f"Part 2: {part2(*vals)}")
