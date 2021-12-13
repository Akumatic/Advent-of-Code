# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/13

class Paper:
    def __init__(self, dots):
        self.max_x = max(dot[0] for dot in dots) + 1
        self.max_y = max(dot[1] for dot in dots) + 1
        self.grid = {dot[1] * self.max_x + dot[0] for dot in dots}

    def __str__(self):
        return "\n".join(
                ["".join(["#" if x+y*self.max_x in self.grid else "." for x in range(self.max_x)]
            ) for y in range(self.max_y)])

    def fold(self, dir: str, idx: int):
        tmp = set()
        for point in self.grid:
            x = point % self.max_x
            y = (point - x) // self.max_x
            if dir == "x" and x < idx:
                tmp.add(x + y * idx)
            elif dir == "x" and x > idx:
                tmp.add(-x + 2*idx + y * idx)
            elif dir == "y" and y < idx:
                tmp.add(x + y * self.max_x)
            elif dir == "y" and y > idx:
                tmp.add(x + (-y + 2*idx) * self.max_x)

        self.grid = tmp
        if dir == "x":
            self.max_x = idx
        else: # dir == "y"
            self.max_y = idx

def read_file(filename: str = "input.txt") -> list:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        lines = [line for line in f.read().strip().split("\n")]
    empty = lines.index("")
    dots = [(int(x[0]), int(x[1])) for x in (s.split(",") for s in lines[:empty])]
    instructions = [(x[0], int(x[1])) for x in (s[11:].split("=") for s in lines[empty+1:])]
    return dots, instructions

def part1(dots: list, folding_instructions: list) -> int:
    paper = Paper(dots)
    paper.fold(*folding_instructions[0])
    return len(paper.grid)

def part2(dots: list, folding_instructions: list) -> int:
    paper = Paper(dots)
    for instruction in folding_instructions:
        paper.fold(*instruction)
    return f"\n{paper}"
    
if __name__ == "__main__":
    vals = read_file() # vals[0] are the dots, vals[1] the folding instructions
    print(f"Part 1: {part1(*vals)}")
    print(f"Part 2: {part2(*vals)}")
