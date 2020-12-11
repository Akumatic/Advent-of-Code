# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
#https://adventofcode.com/2020/day/11

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [list(line.strip()) for line in f.readlines()]

def get_positions(seats: list, x: int, y: int, rx: range, ry: range, adjacent: bool) -> list:
    if adjacent: # check only adjacent tiles
        positions = [(x+i, y+j) for i in range(-1,2) for j in range(-1,2) if (i,j) != (0,0)]
    
    else: # check first seat available in direction
        positions = []
        for dx in range(-1,2):
            for dy in range(-1,2):
                if dx == 0 and dy == 0:
                    continue
                i, j = x, y
                while i + dx in rx and j + dy in ry:
                    i += dx
                    j += dy
                    if seats[i][j] in ("L", "#"):
                        positions.append((i, j))
                        break

    return positions

def count(seats: list, x: int, y: int, seat: str, adjacent: bool) -> int:
    rx, ry =  range(len(seats)), range(len(seats[0]))
    positions = get_positions(seats, x, y, rx, ry, adjacent)
    return sum(1 for pos in positions if pos[0] in rx and pos[1] in ry and \
        seats[pos[0]][pos[1]] == seat)

def iterate(seats: list, adjacent: bool = True) -> list:
    size_outer = len(seats)
    size_inner = len(seats[0])
    while True:
        tmp = [s[:] for s in seats]

        for x in range(size_outer):
            for y in range(size_inner):
                if seats[x][y] == ".":
                    continue

                elif seats[x][y] == "L":
                    if count(seats, x, y, "#", adjacent) == 0:
                        tmp[x][y] = "#"

                else: # seats[x][y] == "#":
                    tolerance = 4 if adjacent else 5
                    if count(seats, x, y, "#", adjacent) >= tolerance:
                        tmp[x][y] = "L"

        if seats == tmp:
            return seats
        else:
            seats = tmp

def part1(input: list) -> int:
    seats = iterate(input)
    return sum([row.count("#") for row in seats])

def part2(input: list) -> int:
    seats = iterate(input, adjacent=False)
    return sum([row.count("#") for row in seats])

if __name__ == "__main__":
    input = readFile()
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")