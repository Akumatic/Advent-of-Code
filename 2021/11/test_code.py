# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import part1, part2, read_file, create_octopuses, step

def test():
    vals = read_file("test_input.txt")
    octopuses = create_octopuses(vals)
    flashes = 0
    for _ in range(10):
        flashes += step(octopuses)
    assert flashes == 204
    print("Passed Test with 10 Iterations")
    assert part1(vals) == 1656
    print("Passed Part 1")
    assert part2(vals) == 195
    print("Passed Part 2")

if __name__ == "__main__":
    test()
