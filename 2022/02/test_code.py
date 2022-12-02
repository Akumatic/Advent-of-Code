# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic

from code import map_moves, part1, part2

def test():
    vals = [map_moves(moves) for moves in [["A", "Y"], ["B", "X"], ["C", "Z"]]]
    assert part1(vals) == 15
    print("Passed Part 1")
    assert part2(vals) == 12
    print("Passed Part 2")

if __name__ == "__main__":
    test()
