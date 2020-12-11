# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic
#
#https://adventofcode.com/2020/day/11

def readFile() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt", "r") as f:
        return [list(line.strip()) for line in f.readlines()]

def get_positions(seats: list, cache: dict, x: int, y: int):
    idx = (x, y)
    cache[idx] = {"adjacent": [], "next_seat": []}

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            # adjacent tiles
            cache[idx]["adjacent"].append((x + dx, y + dy))

            # next available seat
            i, j = x, y
            while i + dx in cache["rx"] and j + dy in cache["ry"]:
                i += dx
                j += dy
                if seats[i][j] in ("L", "#"):
                    cache[idx]["next_seat"].append((i, j))
                    break

def count(seats: list, cache: dict, x: int, y: int, seat: str, selection: str) -> int:
    return sum(1 for pos in cache[(x, y)][selection] if pos[0] in cache["rx"] and \
        pos[1] in cache["ry"] and seats[pos[0]][pos[1]] == seat)

def create_cache(seats: list) -> dict:
    cache = {"rx": range(len(seats)), "ry": range(len(seats[0]))}
    for x in cache["rx"]:
        for y in cache["ry"]:
            get_positions(seats, cache, x, y)
    return cache

def iterate(seats: list, cache: dict, adjacent: bool = True) -> list:
    selection = "adjacent" if adjacent else "next_seat"
    tolerance = 4 if adjacent else 5
    while True:
        tmp = [s[:] for s in seats]

        for x in cache["rx"]:
            for y in cache["ry"]:
                if seats[x][y] == ".":
                    continue

                elif seats[x][y] == "L":
                    if count(seats, cache, x, y, "#", selection) == 0:
                        tmp[x][y] = "#"

                else: # seats[x][y] == "#":
                    if count(seats, cache, x, y, "#", selection) >= tolerance:
                        tmp[x][y] = "L"

        if seats == tmp:
            return seats
        else:
            seats = tmp

def part1(input: list, cache) -> int:
    seats = iterate(input, cache)
    return sum([row.count("#") for row in seats])

def part2(input: list, cache) -> int:
    seats = iterate(input, cache, adjacent=False)
    return sum([row.count("#") for row in seats])

if __name__ == "__main__":
    input = readFile()
    cache = create_cache(input)
    print(f"Part 1: {part1(input, cache)}")
    print(f"Part 2: {part2(input, cache)}")