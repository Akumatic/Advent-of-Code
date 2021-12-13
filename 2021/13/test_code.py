# SPDX-License-Identifier: MIT
# Copyright (c) 2021 Akumatic

from code import part1, part2, read_file, Paper

def test():
    vals = read_file("test_input.txt")
    paper = Paper(vals[0])
    for instruction in vals[1]:
        paper.fold(*instruction)
    assert str(paper) == "#####\n#...#\n#...#\n#...#\n#####\n.....\n....."
    print("Passed folding test")

if __name__ == "__main__":
    test()
