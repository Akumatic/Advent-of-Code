# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic
#
# https://adventofcode.com/2021/day/20

def read_file(filename: str = "input.txt") -> tuple:
    with open(f"{__file__.rstrip('code.py')}{filename}", "r") as f:
        lines = [line for line in f.read().strip().split("\n")]
    algorithm = list(lines[0])
    image = {(x,y - 2):lines[y][x] for x in range(len(lines[2])) for y in range(2, len(lines))}
    return image, algorithm

def step(image: dict, algorithm: list, default: str) -> dict:
    min_point = min(image.keys())
    max_point = max(image.keys())
    new_image = dict()
    for y in range(min_point[1] - 1, max_point[1] + 2):
        for x in range(min_point[0] - 1, max_point[0] + 2):
            tmp = [image.get((i, j), default) for j in (y-1, y, y+1) for i in (x-1, x, x+1)]
            idx = int("".join(["0" if i == "." else "1" for i in tmp]), 2)
            new_image[(x, y)] = algorithm[idx]
    return new_image

def get_light_pixels_after_iterations(image: dict, algorithm: list, iterations: int) -> int:
    for i in range(iterations):
        default = "." if algorithm[0] == "." or i % 2 == 0 else "#"
        image = step(image, algorithm, default)
    return list(image.values()).count("#")

def part1(image: dict, algorithm: list) -> int:
    return get_light_pixels_after_iterations(image, algorithm, 2)
    
def part2(image: dict, algorithm: list) -> int:
    return get_light_pixels_after_iterations(image, algorithm, 50)
        
if __name__ == "__main__":
    vals = read_file()
    print(f"Part 1: {part1(*vals)}")
    print(f"Part 2: {part2(*vals)}")
    