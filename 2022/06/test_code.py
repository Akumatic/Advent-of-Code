# SPDX-License-Identifier: MIT
# Copyright (c) 2022 Akumatic

from code import part1, part2

def test():
    inputs = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", "bvwbjplbgvbhsrlpgdmjqwftvncz", 
    "nppdvjthqldpwncqszvftbrmjlhg", "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]
    expected_values = [(7, 19), (5, 23), (6, 23), (10, 29), (11, 26)]
    for i in range(len(inputs)):
        assert part1(inputs[i]) == expected_values[i][0]
    print("Passed Part 1")
    for i in range(len(inputs)):
        assert part2(inputs[i]) == expected_values[i][1]
    print("Passed Part 2")

if __name__ == "__main__":
    test()
