# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import *

def test():
    scanner = read_file("test_input_1.txt")[0]
    tranformations = [
        [[-1, -1, 1], [-2, -2, 2], [-3, -3, 3], [-2, -3, 1], [5, 6, -4], [8, 0, 7]],
        [[1, -1, 1], [2, -2, 2], [3, -3, 3], [2, -1, 3], [-5, 4, -6], [-8, -7, 0]],
        [[-1, -1, -1], [-2, -2, -2], [-3, -3, -3], [-1, -3, -2], [4, 6, 5], [-7, 0, 8]],
        [[1, 1, -1], [2, 2, -2], [3, 3, -3], [1, 3, -2], [-4, -6, 5], [7, 0, 8]],
        [[1, 1, 1], [2, 2, 2], [3, 3, 3], [3, 1, 2], [-6, -4, -5], [0, 7, -8]]
    ]
    for transformation in tranformations:
        assert transformation in scanner.transformations.values()
    print("Transformation passed")

    scanners = read_file("test_input_2.txt")
    find_scanner_positions(scanners)
    assert scanners[0].get_position() == (0, 0, 0)
    assert scanners[1].get_position() == (68,-1246,-43)
    assert scanners[2].get_position() == (1105,-1205,1229)
    assert scanners[3].get_position() == (-92,-2380,-20)
    print("Passed position finding")
    
    assert part1(scanners) == 79
    print("Passed Part 1")
    assert part2(scanners) == 3621
    print("Passed Part 2")

if __name__ == "__main__":
    test()
